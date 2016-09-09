from django.db import models


class Contact(models.Model):
    user = models.ForeignKey('User')
    name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10, primary_key=True)
    email = models.EmailField(max_length=254, blank=True)
    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    pin_code = models.CharField(max_length=6, blank=True)


class Provider(models.Model):
    provider_name = models.CharField(max_length=30)
    series_list = models.CommaSeparatedIntegerField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, primary_key=True)
    phone_no = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
