from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from versionedPagos.models import Payment, Services, Expired_payments
from .serializers import PaymentSerializer, ServiceSerializer, ExpiredPaymentsSerializer
from .pagination import StandardResultsSetPagination

class PaymentsViewSet(viewsets.ModelViewSet):
  queryset = Payment.objects.all()
  pagination_class = StandardResultsSetPagination
  # serializer_class = PaymentSerializer

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

class ExpiredPaymentsViewSet(viewsets.ModelViewSet):
  queryset = Expired_payments.objects.all()
  serializer_class = ExpiredPaymentsSerializer