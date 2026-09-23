from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_list(request):
    contacts_qs = Contact.objects.all().order_by('name')
    paginator = Paginator(contacts_qs, 10)
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


def contact_detail(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, "contacts/contact_detail.html", {"contact": contact})


def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect("contact_detail", id=contact.id)
    else:
        form = ContactForm()
    return render(request, "contacts/contact_form.html", {"form": form})


def contact_update(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            return redirect("contact_detail", id=contact.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/contact_form.html", {"form": form})

def contact_delete(request, id):
    contact = get_object_or_404(Contact, id = id)
    if request.method == "POST":
        contact.delete()
        return redirect("contact_list")
    return render(request, "contacts/contact_delete.html", {"contact": contact})
