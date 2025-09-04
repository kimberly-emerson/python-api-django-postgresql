"""
tba
"""
from urllib.parse import urlencode, urlparse, parse_qs, urlunparse, urljoin
from collections import OrderedDict


class HATEOASMixin:
    """
    HATEOASMixin for DRF with:
    - Top-level links toggle: include_links=true|false
    - Pagination aware (page_size)
    - Sparse fields via fields query param
    - Item-level links with full CRUD and previous/next
    """

    def finalize_response(self, request, response, *args, **kwargs):
        self.request = request
        self._basename = getattr(self, 'basename', None) or getattr(self, '_basename', None)
        self._lookup_field = getattr(self, 'lookup_field', 'id')

        include_links = request.query_params.get('include_links', 'true').lower() != 'false'
        fields = request.query_params.get('fields')
        page_size = request.query_params.get('page_size')

        # Apply sparse fields
        if fields and response.status_code == 200 and isinstance(response.data, dict):
            self._apply_sparse_fields(response.data, fields.split(','))

        # Always apply item-level HATEOAS links
        if response.status_code == 200 and isinstance(response.data, dict):
            list_key = self._detect_list_key(response.data)
            if list_key:
                items = response.data[list_key]
                for i, item in enumerate(items):
                    item["links"] = self._build_item_links(items, i)
                if include_links:
                    response.data = self._reorder_with_links(response.data, list_key, page_size)
            elif self._lookup_field in response.data:
                response.data["links"] = self._build_item_links([response.data], 0)

        return super().finalize_response(request, response, *args, **kwargs)

    # -----------------------
    # Helpers
    # -----------------------

    def _detect_list_key(self, data):
        for key in ("results", "data"):
            if key in data and isinstance(data[key], list):
                return key
        for key, value in data.items():
            if isinstance(value, list) and value and isinstance(value[0], dict):
                return key
        return None

    def _apply_sparse_fields(self, data, allowed_fields):
        list_key = self._detect_list_key(data)
        if list_key:
            for i, item in enumerate(data[list_key]):
                data[list_key][i] = {k: v for k, v in item.items() if k in allowed_fields}
        elif isinstance(data, dict):
            keys_to_remove = set(data.keys()) - set(allowed_fields)
            for k in keys_to_remove:
                data.pop(k, None)

    def _build_item_links(self, items, index):
        links = []
        item = items[index]
        lookup_value = item.get(self._lookup_field)

        base_url = self.request.build_absolute_uri(self.request.path)

        # If lookup value exists, add detail links
        if lookup_value:
            detail_url = urljoin(base_url + "/", str(lookup_value))
            links.append({"href": detail_url, "rel": "self", "method": "GET"})
            links.append({"href": base_url, "rel": "list", "method": "GET"})
            links.append({"href": base_url, "rel": "create", "method": "POST"})
            links.append({"href": detail_url, "rel": "update", "method": "PUT"})
            links.append({"href": detail_url, "rel": "patch", "method": "PATCH"})
            links.append({"href": detail_url, "rel": "delete", "method": "DELETE"})
        else:
            # Fallback: only safe top-level links
            links.append({"href": base_url, "rel": "list", "method": "GET"})
            links.append({"href": base_url, "rel": "create", "method": "POST"})

        # Previous / next
        if index > 0:
            prev_lookup = items[index - 1].get(self._lookup_field)
            if prev_lookup:
                links.append({
                    "href": urljoin(base_url + "/", str(prev_lookup)),
                    "rel": "previous",
                    "method": "GET",
                })
        if index < len(items) - 1:
            next_lookup = items[index + 1].get(self._lookup_field)
            if next_lookup:
                links.append({
                    "href": urljoin(base_url + "/", str(next_lookup)),
                    "rel": "next",
                    "method": "GET",
                })

        return links

    def _build_top_level_links(self, data, page_size=None):
        links = []
        base_url = self.request.build_absolute_uri(self.request.path)

        # Always include the current request as the "self" link
        links.append({"href": base_url, "rel": "self", "method": "GET"})

        next_link = data.get("next")
        prev_link = data.get("previous")
        count = data.get("count")
        results = data.get("results") or data.get("data")

        if count is not None and results is not None:
            page_size_int = int(page_size) if page_size else len(results)
            from math import ceil
            total_pages = ceil(count / page_size_int) if page_size_int else 1

            def replace_page(page_num):
                parsed = urlparse(base_url)
                query = parse_qs(parsed.query)
                query["page"] = [str(page_num)]
                if page_size_int:
                    query["page_size"] = [str(page_size_int)]
                return urlunparse(parsed._replace(query=urlencode(query, doseq=True)))

            links.append({"href": replace_page(1), "rel": "first", "method": "GET"})
            links.append({"href": replace_page(total_pages), "rel": "last", "method": "GET"})
            if next_link:
                links.append({"href": next_link, "rel": "next", "method": "GET"})
            if prev_link:
                links.append({"href": prev_link, "rel": "previous", "method": "GET"})

        return links

    def _reorder_with_links(self, data, list_key, page_size=None):
        top_links = self._build_top_level_links(data, page_size)
        ordered = OrderedDict()
        if "count" in data:
            ordered["count"] = data["count"]
        ordered["links"] = top_links
        ordered[list_key] = data[list_key]
        for key, value in data.items():
            if key not in ordered:
                ordered[key] = value
        return ordered
