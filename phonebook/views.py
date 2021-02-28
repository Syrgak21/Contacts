from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Contact


def main(request):
    contacts_list = Contact.objects.all()
    paginator = Paginator(contacts_list, 5)

    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)
    return render(request, 'main.html', context = {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            name = request.POST['fullname'],
            number = request.POST['number'],
            email = request.POST['email'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'add.html', context={})

def detail_contact(request, pk):
    detail = Contact.objects.get(id=pk)
    if request.method == 'POST':
        detail.name = request.POST['fullname']
        detail.number = request.POST['number']
        detail.email = request.POST['email']
        detail.address = request.POST['address']
        detail.save()
        return redirect('/')
    return render(request, 'detail.html', context={'detail':detail})

def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', context={'contact':contact})
