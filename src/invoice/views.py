from datetime import datetime

from django.shortcuts import redirect
from django.views.generic import ListView

from invoice.forms import ClientForm, ProductForm, InvoiceForm, CompanyForm
from invoice.models import Client, Invoice, Product, Company


class Dashboard(ListView):
    model = Client
    template_name = 'invoice/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all().count()
        context['invoices'] = Invoice.objects.all().count()
        context['paid_invoices'] = Invoice.objects.filter(status='PAID').count()
        return context


class Products(ListView):
    model = Product
    template_name = 'invoice/products.html'

    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['form'] = ProductForm()
        return context

    def post(self, request, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('invoice:products')


class Clients(ListView):
    model = Client
    template_name = 'invoice/clients.html'

    def get_context_data(self, **kwargs):
        context = super(Clients, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['form'] = ClientForm()
        return context

    def post(self, request, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('invoice:clients')


class Invoices(ListView):
    model = Invoice
    template_name = 'invoice/invoices.html'

    def get_context_data(self, **kwargs):
        context = super(Invoices, self).get_context_data(**kwargs)
        context['invoices'] = Invoice.objects.all()
        context['form'] = InvoiceForm()
        return context

    def post(self, request, **kwargs):
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('invoice:clients')


class CompanySettings(ListView):
    model = Company
    template_name = 'invoice/company-settings.html'

    def get_context_data(self, **kwargs):
        context = super(CompanySettings, self).get_context_data(**kwargs)
        context['company'] = Company.objects.get()
        context['form'] = CompanyForm()
        return context

    def post(self, request, **kwargs):
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('invoice:company')


""""""


class CreateInvoice(ListView):
    year = datetime.now().strftime("%Y")
    month = datetime.now().strftime("%m")
    number_of_invoice = Invoice.objects.filter(date_created__year=year, date_created__month=month).count()


class CreateBuildInvoice(ListView):
    pass


class DeleteInvoice(ListView):
    pass
