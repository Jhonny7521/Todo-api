from rest_framework import serializers
from versionedPagos.models import Services, Payment, Expired_payments

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Services
    fields = '__all__'
    read_only_fields = '__all__',


class PaymentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payment
    fields = ('__all__')


class ExpiredPaymentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Expired_payments
    fields = '__all__'