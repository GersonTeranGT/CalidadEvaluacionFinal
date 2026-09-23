from django.urls import path
from .views import *

urlpatterns = [
    path('', contact_list, name="contact_list"),
    path("contact/<int:id>", contact_detail, name = "contact_detail"),
    path("contact/create", contact_create, name = "contact_create"),
    path("contact/update/<int:id>", contact_update, name = "contact_update"),
    path("contact/delete/<int:id>", contact_delete, name = "contact_delete"),
]