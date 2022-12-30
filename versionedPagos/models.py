from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

# Create your models here.

class Services(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=255)
  logo = models.URLField(null=True)
  creado_en = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name


class Payment(models.Model):

  User_id = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users_id')
  Service_id = models.ForeignKey(Services, on_delete =models.CASCADE, related_name='services_id')
  Amount = models.FloatField(default=0.0)
  PaymentDate = models.DateField(null=True)
  ExpirationDate = models.DateField(null=True)

  def __str__(self):
    return f'Fecha de expiración: {self.PaymentDate}, monto de {self.Amount}'


class Expired_payments(models.Model):
  Payment_user_id = models.ForeignKey(Payment, on_delete =models.CASCADE, related_name='payment_expired')
  Penalty_fee_amount = models.FloatField(default=0.0)
  

  def __str__(self):
    return self.Penalty_fee_amount