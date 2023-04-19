from django.urls import path
from Accounts.views import *
urlpatterns = [
    path('owner',owner,name="owner-queries"),
    path('staff',staff,name="staff-queries"),
    path('manager',manager,name="manager-queries"),
    path('property',property,name="property-queries"),
    path('branch',branch,name="branch-queries"),
    path('client',client,name="client-queries")
]

