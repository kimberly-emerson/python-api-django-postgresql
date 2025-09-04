"""
tba
"""

from rest_framework import serializers

from api.people.models.address_type_model import AddressType
from api.utils.hateoas_serializer import HATEOASLinkSerializer


class AddressTypeSerializer(serializers.ModelSerializer):
    """
    tba
    """
    class Meta:
        """
        tba
        """

        model = AddressType
        fields = '__all__'
        read_only_fields = [
            'address_type_id',
            'rowguid',
            'modified_date',
        ]


class AddressTypeListResponseSerializer(serializers.Serializer):
    """
    tba
    """
    count = serializers.IntegerField()
    links = HATEOASLinkSerializer(many=True)
    data = AddressTypeSerializer(many=True)


class AddressTypeDetailResponseSerializer(serializers.Serializer):
    """
    tba
    """
    links = HATEOASLinkSerializer(many=True)
    data = AddressTypeSerializer()
