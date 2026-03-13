import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Enquiry, Product

PAGES = [
    {
        "title": "Home | S&B Spices",
        "heading": "100% NATURAL CARDAMOM",
        "description": "Our 100% natural cardamom is grown without artificial additives, preserving its pure aroma, authentic flavor, and natural goodness for the highest quality experience.",
        "bg_image": "bg1.jpg",
    },
    {
        "title": "Our Products | S&B Spices",
        "heading": "SPICES FROM THE HILLS",
        "description": "Handpicked and fresh from high-altitude plantations, our spices bring the authentic flavor of nature to your kitchen.",
        "bg_image": "bg2.jpg",
    },
    {
        "title": "Quality & Export | S&B Spices",
        "heading": "PREMIUM QUALITY EXPORT",
        "description": "Strict quality checks ensuring bold aroma and global export standards.",
        "bg_image": "bg3.jpg",
    },
]


def home(request):
    top_products = Product.objects.all()[:3]
    context = {
        "pages": PAGES,
        "pages_json": json.dumps(PAGES),
        "products": top_products,
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def products(request):
    search = request.GET.get("search", "").strip()
    queryset = Product.objects.all()

    if search:
        queryset = queryset.filter(name__icontains=search)

    return render(request, "products.html", {"products": queryset, "search": search})


def enquiry(request):
    if request.method != "POST":
        return redirect("home")

    Enquiry.objects.create(
        name=request.POST.get("name", "").strip(),
        company=request.POST.get("company", "").strip(),
        place=request.POST.get("country", "").strip(),
        email=request.POST.get("email", "").strip(),
        phone=request.POST.get("phone", "").strip(),
        grade=request.POST.get("grade", "").strip(),
    )
    messages.success(request, "Submitted successfully!")
    return redirect("home")


def login_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("/admin/")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect("/admin/")

        messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")
