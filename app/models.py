from django.db import models
from django import forms
from django.core import validators

def check_for_a(data):
    if data.lower()[0]=='a':
        raise forms.ValidationError('Invalid data')

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=10)
    sage=models.IntegerField()
    smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def __str__(self):
        return self.sname
