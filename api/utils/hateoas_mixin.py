"""
tba
"""


class HATEOASMixin:
    """
    Adds HATEOAS links to serializer output.
    """
    # pylint: disable=unused-argument
    def get_links(self, obj):
        """
        Override this in subclasses to define links.
        """
        return {}

    def to_representation(self, instance):
        """
        tba
        """
        rep = super().to_representation(instance)
        request = self.context.get("request")

        if request:
            rep["_links"] = self.get_links(instance)
        return rep
