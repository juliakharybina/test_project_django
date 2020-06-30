from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.constraints import CheckConstraint, Q


class Period(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Active', 'Active'),
        ('Reconciliation', 'Reconciliation'),
        ('Closed', 'Closed'),
    )
    start_date_period = models.DateTimeField(blank=True)
    stop_date_period = models.DateTimeField(blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.stop_date_period)

    def clean(self):
        if self.start_date_period > self.stop_date_period:
            raise ValidationError('Start date must be before stop_date')


class Country(models.Model):
    code = models.CharField(max_length=3, null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=100, null=True)
    id_country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Negotiator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Agreement(models.Model):
    id_negotiator = models.ForeignKey(Negotiator, null=True, on_delete=models.SET_NULL)
    id_company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(blank=True)
    stop_date = models.DateTimeField(blank=True)
    debit = models.CharField(max_length=100, null=True)
    credit_turnover = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.id)

    def clean(self):
        if self.start_date > self.stop_date:
            raise ValidationError('Start date must be before stop_date')


class Bridge(models.Model):
    id_period = models.ForeignKey(Period, null=True, on_delete=models.SET_NULL)
    id_agreement = models.ForeignKey(Agreement, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)


