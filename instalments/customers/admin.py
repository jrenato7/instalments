from django.contrib import admin

from .models import Client, CreditCard, PurchaseCreditCard, \
    InstalmentsCreditCard


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'activate','created_at']
    list_filter = ['activate']
    search_fields = ['name', 'email']


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ['client', 'nickname', 'banner','valid_date', 
    'closing_day', 'maturity']
    list_filter = ['banner']
    search_fields = ['nickname']


@admin.register(PurchaseCreditCard)
class PurchaseCreditCardAdmin(admin.ModelAdmin):
    list_display = ['card', 'description', 'instalments_number','value', 
        'date']
    search_fields = ['description', 'date']


@admin.register(InstalmentsCreditCard)
class InstalmentsCreditCardAdmin(admin.ModelAdmin):
    list_display = ['purchase', 'value', 'number']
    search_fields = ['purchase']