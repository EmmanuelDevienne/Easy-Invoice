from datetime import datetime
from zoneinfo import ZoneInfo

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Client(models.Model):
    # Basic Fields.
    full_name = models.CharField(null=True, blank=True, max_length=200)
    address_line1 = models.CharField(null=True, blank=True, max_length=200)
    address_line2 = models.CharField(null=True, blank=True, max_length=200)
    postal_code = models.CharField(null=True, blank=True, max_length=10)
    phone_number = models.CharField(null=True, blank=True, max_length=100)
    email_address = models.CharField(null=True, blank=True, max_length=100)
    tax_number = models.CharField(null=True, blank=True, max_length=100)
    clientLogo = models.ImageField(default='default_logo.jpg', upload_to='company_logos')

    # Utility fields
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.full_name} {self.phone_number} {self.email_address}'

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = datetime.now(tz=ZoneInfo("Europe/Paris"))

        self.slug = slugify(f'{self.full_name} {self.phone_number}')
        self.last_updated = datetime.now(tz=ZoneInfo("Europe/Paris"))

        super(Client, self).save(*args, **kwargs)


class Invoice(models.Model):
    TERMS = [
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

    STATUS = [
        ('CURRENT', 'CURRENT'),
        ('EMAIL_SENT', 'EMAIL_SENT'),
        ('OVERDUE', 'OVERDUE'),
        ('PAID', 'PAID'),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    number = models.CharField(null=True, blank=True, max_length=100)
    payment_terms = models.CharField(choices=TERMS, default='14 days', max_length=100)
    due_date = models.DateField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='€', max_length=100)
    amount_vat = models.FloatField(null=True, blank=True)
    exemption_vat = models.CharField(choices=EXEMPTION_VAT, default='€', max_length=100)
    notes = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default='CURRENT', max_length=100)

    # RELATED fields
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)

    # Utility fields
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        if self.last_updated is None:
            date = self.date_created
        else:
            date = self.last_updated
        return f'{date} {self.number} {self.title}'

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = datetime.now(tz=ZoneInfo("Europe/Paris"))

        self.slug = slugify(f'{self.number}')
        self.last_updated = datetime.now(tz=ZoneInfo("Europe/Paris"))

        super(Invoice, self).save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    # Related Fields
    invoice = models.ForeignKey(Invoice, blank=True, null=True, on_delete=models.CASCADE)

    # Utility fields
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.price}'

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = datetime.now(tz=ZoneInfo("Europe/Paris"))

        self.slug = slugify(f'{self.title} {self.price}')
        self.last_updated = datetime.now(tz=ZoneInfo("Europe/Paris"))

        super(Product, self).save(*args, **kwargs)


class Company(models.Model):
    # Basic Fields
    full_name = models.CharField(null=True, blank=True, max_length=200)
    address_line1 = models.CharField(null=True, blank=True, max_length=200)
    address_line2 = models.CharField(null=True, blank=True, max_length=200)
    postal_code = models.CharField(null=True, blank=True, max_length=10)
    phone_number = models.CharField(null=True, blank=True, max_length=100)
    email_address = models.CharField(null=True, blank=True, max_length=100)
    tax_number = models.CharField(null=True, blank=True, max_length=100)
    client_logo = models.ImageField(default='default_logo.jpg', upload_to='my_company_logo')

    # Utility fields
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.full_name}'

    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = datetime.now(tz=ZoneInfo("Europe/Paris"))

        self.slug = slugify(f'{self.full_name}')
        self.last_updated = datetime.now(tz=ZoneInfo("Europe/Paris"))

        super(Company, self).save(*args, **kwargs)
