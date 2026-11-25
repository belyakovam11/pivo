from django.contrib import admin
from django.urls import path

from brewery import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("register/buyer/", views.register_buyer, name="register_buyer"),
    path("register/event/", views.register_event, name="register_event"),
    path("projects/apply/", views.submit_project, name="submit_project"),
]
