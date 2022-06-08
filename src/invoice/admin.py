from django.contrib import admin

from .models import Client, Product, Invoice, Compagny


class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "email_address")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description")


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "due_date", "status")


class CompagnyAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "email_address")


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Compagny, CompagnyAdmin)
