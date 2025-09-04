"""
tba
"""

from rest_framework import serializers

from api.people.models.country_region_model import CountryRegion
from api.sales.models.sales_territory_model import SalesTerritory
from api.people.serializers.country_region_serializer import (
  CountryRegionSerializer
)
from api.utils.hateoas_serializer import HATEOASLinkSerializer


class SalesTerritorySerializer(serializers.ModelSerializer):
    """
    tba
    """
    country_region = serializers.SlugRelatedField(
        slug_field="country_region_code",
        # pylint: disable=no-member
        queryset=CountryRegion.objects.all(),
        write_only=True
    )
    country_region_detail = CountryRegionSerializer(
        source='country_region',
        read_only=True
    )

    class Meta:
        """
        tba
        """

        model = SalesTerritory
        fields = '__all__'
        read_only_fields = [
            'sales_territory_id',
            'rowguid',
            'modified_date',
        ]


class SalesTerritoryListResponseSerializer(serializers.Serializer):
    """
    tba
    """
    count = serializers.IntegerField()
    links = HATEOASLinkSerializer(many=True)
    data = SalesTerritorySerializer(many=True)


class SalesTerritoryDetailResponseSerializer(serializers.Serializer):
    """
    tba
    """
    links = HATEOASLinkSerializer(many=True)
    data = SalesTerritorySerializer()
