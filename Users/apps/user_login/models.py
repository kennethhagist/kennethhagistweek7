# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def create_valid_user():

    user = {}
    print "Enter a First Name"
    user['first_name'] = raw_input()

    print "Enter a Last Name"
    user['last_name'] = raw_input()

    print "Enter an Email Address"
    user['email_address'] = raw_input()

    print "Enter an Age"
    user['age'] = raw_input()

    if is_valid(**user):
        User.objects.create(**user)
        print "successfully created a user"

def is_valid(**kwargs):
    valid = True
    existing = User.objects.filter(email_address=kwargs['email_address'])
    if len(existing) > 0:
        valid = False
        print "Email is already in use"
    if len(kwargs['first_name']) < 3 or len(kwargs['last_name']) < 3:
        valid = False
        print 'Name fields must be at least 3 characters'

    try:
        validate_email(kwargs['email_address'])
    except ValidationError:
        valid = False
        print "invalid email"

    return valid

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.email_address
