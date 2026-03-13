from django.contrib import admin

from .models import Enquiry, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "availability", "grade", "created_at")
    search_fields = ("name", "grade")
    list_filter = ("availability", "grade")


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "place", "email", "phone", "grade", "created_at")
    search_fields = ("name", "company", "email", "phone")
    list_filter = ("grade", "place")


admin.site.site_header = "S&B Spices Admin"
admin.site.site_title = "S&B Admin"
admin.site.index_title = "Manage products and enquiries"
