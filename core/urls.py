from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("products/", views.products, name="products"),
    path("enquiry/", views.enquiry, name="enquiry"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
