from rest_framework import routers

from .api import PaymentsViewSet, ServicesViewSet, ExpiredPaymentsViewSet

router = routers.DefaultRouter()

router.register(r'pagos', PaymentsViewSet, 'pagos_v2')
router.register(r'servicios', ServicesViewSet, 'sevicios')
router.register(r'expired-payments', ExpiredPaymentsViewSet, 'expired_payments')


api_v2_urlpatterns = router.urls