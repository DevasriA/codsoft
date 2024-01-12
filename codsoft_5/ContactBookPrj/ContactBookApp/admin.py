from django.contrib import admin

from ContactBookApp import models

#Display from admin side 
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','mail','phonenumber',)

# Register your models here.
admin.site.register(models.Contact,ContactAdmin)
