from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.form_detail, name="form_detail"),
    path("<slug:slug>/success/", views.form_success, name="form_success"),
]
