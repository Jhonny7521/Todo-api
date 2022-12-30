from django.urls import path, re_path, include
from . import api
from rest_framework import routers

from versionedPagos.v2.router import api_v2_urlpatterns as api_v2

router = routers.DefaultRouter()
router.register(r'api/v1/pagos', api.PagoViewSet, 'pagos_v1')

urlpatterns =[
  re_path(r'^api/v2/', include(api_v2)),
]

urlpatterns += router.urls