from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="shophome"),
   path("about/", views.about, name="AboutUs"),
   path("Contact/", views.contact, name="ContactUs"),
   path("Traker/", views.tracker, name="TrackingStatus"),
   path("search/", views.search, name="Search"),
   path("productview/", views.productview, name="Productview"),
   path("checkout/", views.checkout, name="Checkout")
]
