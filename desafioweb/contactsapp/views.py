from django.shortcuts import render, redirect
from .models import Contact
import math

# Create your views here.
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})

def list(request):
    if 'page' in request.POST:
        page = int(request.POST['page'])
    else:
        page = 1
    if 'limit' in request.POST:
        limit = int(request.POST['limit'])
    else:
        limit = 50

    page_number = []
    number = int(math.ceil(Contact.objects.count()/limit))
    for i in range(1, number+1):
        page_number.append(i)


    list = Contact.objects.all()[page*limit-limit: limit*page]
    return render(request, 'list.html', {'list': list, 'page_number': page_number})

def delete(request, id):
    if id:
        obj = Contact.objects.get(id=id)
        obj.delete()
    return redirect('/list')