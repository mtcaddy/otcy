from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Trade(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('draft', 'Draft'),
    )
    TradeOf = (
        ('Bitcoin', 'BTC'),
        ('Etherem', 'ETH'),
        ('UGX', 'UGX'),
        ('NGN', 'NGN'),
        ('RWF', 'RWF'),
        ('CHF', 'CHF'),
        ('USD', 'USD'),
    )
    title = models.CharField(max_length=250)
    #slug = models.SlugField(max_length=250,unique_for_date='tradetime')
    salesperson = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='trade_user')
    #customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trade_customer')
    exchange_from = models.CharField(max_length=10,
                              choices=TradeOf,
                              default='BTC')
    exchange_to = models.CharField(max_length=10,
                              choices=TradeOf,
                              default='UGX')
    exchange_amount = models.CharField(max_length=20)
    exchange_percentage = models.CharField(max_length=20)
    exchange_fees = models.CharField(max_length=20)
    wallet_source = models.CharField(max_length=20)
    wallet_destination = models.CharField(max_length=43)
    mobilemoney_no = models.CharField(max_length=20)
    whatsapp_no = models.CharField(max_length=15)
    bank_details = models.CharField(max_length=200)
    tradetime = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    customer_feedback = models.TextField()
    comment = models.TextField()

    class Meta:
        ordering = ('-tradetime',)
    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    phone = models.CharField('Contact Phone', max_length=20, blank=False)
    whatsapp = models.CharField('Whatsapp No.', max_length=20, blank=True)
    email_address = models.EmailField('Email Address', blank=True)
    address = models.CharField(max_length=300, blank=True)
    city = models.CharField('City',max_length=30, blank=True)
    zip_code = models.CharField('Zip/Post Code', max_length=12, blank=True)
    country = models.CharField('Country',max_length=300)
    wallet = models.CharField(max_length=43, blank=True)
    web = models.URLField('Web Address', blank=True)

##TODO
# add info of own bit2big wallets
# detect if wallet is valid (check if excist and balance/ past transactions)
# wallet has used before with us? For other user?
# show balanceon own wallets (localbitcoins).
# https://djangobook.com/mdj2-django-admin/
#
