"""
tba
"""

from rest_framework.routers import DefaultRouter

from api.admin.views.user_viewset import UserViewSet
from api.admin.views.group_viewset import GroupViewSet

from api.people.views.address_type_viewset import AddressTypeViewSet
from api.people.views.country_region_viewset import CountryRegionViewSet
# from api.people.views.state_province_viewset import StateProvinceViewSet
from api.sales.views.sales_territory_viewset import SalesTerritoryViewSet


router = DefaultRouter()

router.register(r'api/admin/users', UserViewSet, basename='user')
router.register(r'api/admin/groups', GroupViewSet, basename='group')

router.register(
  r'api/people/address-types',
  AddressTypeViewSet,
  basename='address-types'
)
router.register(
  r'api/people/country-regions',
  CountryRegionViewSet,
  basename='country-regions'
)
# router.register(
#   r'api/people/state-provinces',
#   StateProvinceViewSet,
#   basename='state-provinces'
# )
router.register(
  r'api/sales/sales-territories',
  SalesTerritoryViewSet,
  basename='sales-territories'
)
