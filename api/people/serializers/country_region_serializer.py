"""
tba
"""

from rest_framework import serializers

from api.people.models.country_region_model import CountryRegion
from api.utils.hateoas_serializer import HATEOASLinkSerializer


class CountryRegionSerializer(serializers.ModelSerializer):
    """
    tba
    """

    class Meta:
        """
        tba
        """

        model = CountryRegion
        fields = '__all__'
        read_only_fields = [
            'modified_date',
        ]


class CountryRegionListResponseSerializer(serializers.Serializer):
    """
    tba
    """
    count = serializers.IntegerField()
    links = HATEOASLinkSerializer(many=True)
    data = CountryRegionSerializer(many=True)


class CountryRegionDetailResponseSerializer(serializers.Serializer):
    """
    tba
    """
    links = HATEOASLinkSerializer(many=True)
    data = CountryRegionSerializer()
