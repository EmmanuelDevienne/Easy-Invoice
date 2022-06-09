from django.urls import path

from invoice.views import Dashboard, Products, Clients, Invoices, CompanySettings, CreateInvoice, CreateBuildInvoice, \
    DeleteInvoice

app_name = "invoice"

urlpatterns = [

    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('products', Products.as_view(), name='products'),
    path('clients', Clients.as_view(), name='clients'),
    path('invoices', Invoices.as_view(), name='invoices'),
    path('company', CompanySettings.as_view(), name='company'),

    # Create URL Paths
    path('invoices/create', CreateInvoice.as_view(), name='create-invoice'),
    path('invoices/create-build/<slug:slug>', CreateBuildInvoice.as_view(), name='create-build-invoice'),

    # Delete an invoice
    path('invoices/delete/<slug:slug>', DeleteInvoice.as_view(), name='delete-invoice'),

]
