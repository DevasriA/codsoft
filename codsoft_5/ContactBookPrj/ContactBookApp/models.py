from django.db import models

from django import forms

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    address=models.TextField()
    class Meta:
        db_table='contact'
    def __str__(self):
        return self.name

#Create Form from Models using ModelForm
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
