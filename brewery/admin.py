from django.contrib import admin

from .models import BuyerRegistration, EventRegistration, ProjectApplication


@admin.register(BuyerRegistration)
class BuyerRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "buyer_type", "contact", "company", "created_at")
    list_filter = ("buyer_type", "created_at")
    search_fields = ("name", "contact", "company")


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ("event_title", "name", "contact", "guests", "created_at")
    list_filter = ("event_title", "created_at")
    search_fields = ("name", "contact")


@admin.register(ProjectApplication)
class ProjectApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "created_at")
    search_fields = ("name", "contact", "idea")
