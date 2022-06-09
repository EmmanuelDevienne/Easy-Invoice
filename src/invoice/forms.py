from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms

from invoice.models import Client, Product, Invoice, Company


class DateInput(forms.DateInput):
    input_type = 'date'


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'address_line1', 'address_line2', 'postal_code', 'phone_number', 'email_address',
                  'tax_number', 'clientLogo']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'quantity', 'price']


class InvoiceForm(forms.ModelForm):
    THE_OPTIONS = [
        ('14 days', '14 days'),
        ('30 days', '30 days'),
        ('60 days', '60 days'),
    ]
    CURRENCY = [
        ('€', 'EUR'),
        ('$', 'USD'),
    ]
    EXEMPTION_VAT = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    STATUS_OPTIONS = [
        ('CURRENT', 'CURRENT'),
        ('OVERDUE', 'OVERDUE'),
        ('PAID', 'PAID'),
    ]

    title = forms.CharField(
        required=True,
        label='Invoice Name or Title',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Title'}), )
    payment_terms = forms.ChoiceField(
        choices=THE_OPTIONS,
        required=True,
        label='Select Payment Terms',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}), )
    currency = forms.ChoiceField(
        choices=CURRENCY,
        required=True,
        label='Select Currency',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}), )
    amount_vat = forms.CharField(
        required=False,
        label='VAT Amount',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Your VAT Amount'}), )
    exemption_vat = forms.ChoiceField(
        choices=EXEMPTION_VAT,
        required=True,
        label='Exemption of VAT',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}), )
    notes = forms.CharField(
        required=False,
        label='Enter any notes for the client',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))
    status = forms.ChoiceField(
        choices=STATUS_OPTIONS,
        required=True,
        label='Change Invoice Status',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}), )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('currency', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('exemption_vat', css_class='form-group col-md-6'),
                Column('amount_vat', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('payment_terms', css_class='form-group col-md-6'),
                Column('status', css_class='form-group col-md-6'),
                css_class='form-row'),
            'notes',

            Submit('submit', ' SAVE INVOICE '))

    class Meta:
        model = Invoice
        fields = ['title', 'payment_terms', 'currency', 'amount_vat', 'exemption_vat', 'status', 'notes']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['full_name', 'address_line1', 'address_line2', 'postal_code', 'phone_number', 'email_address',
                  'tax_number', 'client_logo']


class ClientSelectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.initial_client = kwargs.pop('initial_client')
        self.CLIENT_LIST = Client.objects.all()
        self.CLIENT_CHOICES = [('-----', '--Select a Client--')]

        for client in self.CLIENT_LIST:
            d_t = client.full_name
            self.CLIENT_CHOICES.append(d_t)

        super(ClientSelectForm, self).__init__(*args, **kwargs)

        self.fields['client'] = forms.ChoiceField(
            label='Choose a related client',
            choices=self.CLIENT_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control mb-3'}), )

    class Meta:
        model = Invoice
        fields = ['client']

    def clean_client(self):
        c_client = self.cleaned_data['client']
        if c_client == '-----':
            return self.initial_client
        else:
            return Client.objects.get(uniqueId=c_client)
