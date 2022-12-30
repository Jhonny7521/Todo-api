from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle

from versionedPagos.models import Payment, Services, Expired_payments
from .serializers import PaymentSerializer, ServiceSerializer, ExpiredPaymentsSerializer
from .pagination import StandardResultsSetPagination
from .permissions import ServicePermission, CustomPermission

class PaymentsViewSet(viewsets.ModelViewSet):
  queryset = Payment.objects.all()
  pagination_class = StandardResultsSetPagination
  permission_classes = [IsAuthenticated, CustomPermission]
  filter_backends = [SearchFilter]
  search_fields = ['PaymentDate', 'ExpirationDate']

  throttle_scope = 'pagos'

  def get_serializer_class(self):
    return PaymentSerializer

  def list(self, request):
    # insert_data()
    page = self.paginate_queryset(self.queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = Payment.objects.all()
    todo = get_object_or_404(queryset, pk=pk)
    serializer = PaymentSerializer(todo)
    return Response(serializer.data)
  
  def create(self, request):
    datos = request.data
    print(request.data)
    if isinstance(request.data, list):
      serializer = PaymentSerializer(data=request.data, many = True)
    else:
      serializer = PaymentSerializer(data=request.data)

    print(serializer)
    if serializer.is_valid():
      payment = serializer.save()
      if payment.PaymentDate > payment.ExpirationDate:
        Expired_payments.objects.create(Payment_user_id=payment, Penalty_fee_amount=30.0)

      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def update(self, request, pk=None):
    queryset = Payment.objects.all()
    todo = get_object_or_404(queryset, pk=pk)
    serializer = PaymentSerializer(todo, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def partial_update(self, request, pk=None):
    queryset = Payment.objects.all()
    todo = get_object_or_404(queryset, pk=pk)
    serializer = PaymentSerializer(todo, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=None):
    queryset = Payment.objects.all()
    todo = get_object_or_404(queryset, pk=pk)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ServicesViewSet(viewsets.ModelViewSet):
  queryset = Services.objects.all()
  serializer_class = ServiceSerializer
  permission_classes = [IsAuthenticated, ServicePermission]

  throttle_scope = 'servicesAndExpiredPayments'

class ExpiredPaymentsViewSet(viewsets.ModelViewSet):
  queryset = Expired_payments.objects.all()
  serializer_class = ExpiredPaymentsSerializer
  permission_classes = [IsAuthenticated, CustomPermission]

  throttle_scope = 'servicesAndExpiredPayments'