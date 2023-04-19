from django.contrib import admin
from django.urls import path, include
from Accounts.views import home


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home,name='home'),
    path('queries/',include('Accounts.urls')),
    path("__reload__/", include("django_browser_reload.urls"))
]
