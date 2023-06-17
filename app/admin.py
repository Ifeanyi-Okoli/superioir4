from django.contrib import admin

from django.contrib.auth.models import User

from .models import Profile

from django.contrib.admin import AdminSite

# Register your models here.

ADMIN_SITE_TITLE = "Superior4 - Admin"
ADMIN_SITE_HEADER = "Superior4"

admin.site.register(Profile)

# class EventAdminSite(AdminSite):
#     site_header = 'Superior4 Executive Admin'
#     site_title = 'Superior4 Executive Admin Portal'
#     index_title = 'Welcome to Superior4 Admin Portal'
    
    
# event_admin_site = EventAdminSite(name = 'event_admin')

# event_admin_site.register(User)


class EventAdminSite(admin.AdminSite):
    site_header = 'Superior4 Executive Admin'
    site_title = 'Superior4 Executive Admin Portal'
    index_title = 'Welcome to Superior4 Admin Portal'
    
    
event_admin_site = EventAdminSite(name = 'SuperAdmin')

event_admin_site.register(User)