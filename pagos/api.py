from rest_framework import viewsets, filters 
from rest_framework.permissions import IsAuthenticated

from .models import Pagos
from .serializers import PagoSerializer
from .pagination import StandardResultsSetPagination


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.get_queryset().order_by('id')
    serializer_class = PagoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    # permission_classes = [IsAuthenticated]

    search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'


#     "tokens": {
#"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMTg5NjQ4LCJpYXQiOjE2NzIxODkzNDgsImp0aSI6ImY0ZGI5NjIzMGM3YjQ3OWM4ZDc4NmE4ZmExYTUxN2E4IiwidXNlcl9pZCI6Mn0.R-5L1kifg0siMurTFdC9Hz_U59xfrbKETMCUHXG0on4",
#"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MjI3NTc0OCwiaWF0IjoxNjcyMTg5MzQ4LCJqdGkiOiI4ZmZhZjNmNzU4MzU0YWIzYTM2MzEzOTU1NGZjZjQ1YiIsInVzZXJfaWQiOjJ9.M_RaDJVeksES62T9G4CEAiDKpDIB3sQCwIp0bvJpNnk"
# }