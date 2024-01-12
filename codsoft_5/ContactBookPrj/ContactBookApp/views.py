from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from ContactBookApp.models import Contact, ContactForm

from django.template import loader
from django.urls import reverse


# Create your views here.

#view : base template
def home(request):
    return render(request,'index.html',{})

#Read all contacts
def contactlist(request):
    ct=Contact.objects.all()
    return render(request,'listall.html',{'contacts':ct})
#CRUD operations  
#Create a contact
def createct(request):
    if request.method == 'POST':
        frm = ContactForm(request.POST)
        if frm.is_valid():
            nwct=frm.save() #form input save
            #nwct.save()# db table save
        return render(request,'contactfrm.html',{'newcontact':nwct,'frm':ContactForm()})
    else:
        return render(request,'contactfrm.html',{'frm':ContactForm()})

#Read single/specific contact
def contactdetails(request, id):
    mymember = Contact.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {'mymember': mymember,}
    return HttpResponse(template.render(context, request))

#Update a contact
def updatect(request, id):
    ct=Contact.objects.get(id=id)
    if request.method == 'POST':
        frm = ContactForm(request.POST, instance=ct)
        if frm.is_valid():
            contupt=frm.save() #form input save
            contupt.save()# db table save
            return HttpResponseRedirect(reverse('contactlist'))
    else:
        frm = ContactForm(instance=ct)
    return render(request,'contactupdate.html',{'frm':frm})


#Delete a contact
def deletect(request, id):
    ct = Contact.objects.get(id=id)
    ct.delete()
    return HttpResponseRedirect(reverse('contactlist'))

#Search a contact by name
def search(request):
    #Search a specific entry
    if request.method == 'POST':
        cname=request.POST['name']
        ct=Contact.objects.filter(name__contains=cname)
        return render(request,'contactsrch.html',{'results':cname,'contacts':ct})
    else:
        return render(request,'contactsrch.html',{})

