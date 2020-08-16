from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Tradestatus(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('sent', 'Sent'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='tradetime')
    salesperson = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='trade_posts')
    body = models.TextField()
    tradetime = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    class Meta:
        ordering = ('-tradetime',)
    def __str__(self):
        return self.title
