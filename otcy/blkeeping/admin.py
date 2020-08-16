from django.contrib import admin
from .models import Contact, Trade
# Register your models here.

#@admin.register(Contact)
#class ContactAdmin(admin.ModelAdmin):
#	list_display = ('first_name', 'last_name')
#	ordering = ('first_name',)
#	search_fields = ('first_name', 'last_name', 'wallet')


#@admin.register(Trade)
#class TradeAdmin(admin.ModelAdmin):
#	list_display = ('first_name', 'last_name','mobilemoney_no')
#	ordering = ('tradetime',)
#	search_fields = ('first_name', 'last_name', 'wallet')


admin.site.register(Contact)
admin.site.register(Trade)
