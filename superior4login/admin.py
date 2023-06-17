from django.contrib import admin
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'Superior4'
    

custom_admin_site = CustomAdminSite()
admin.site = custom_admin_site