from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from app.admin import event_admin_site
from django.contrib import staticfiles
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='portal.html'), name='portal'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('gallery/', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path('products/', TemplateView.as_view(template_name='products.html'), name='products'),
    path('documentation/', TemplateView.as_view(template_name='documentation.html'), name='documentation'),
    path('exec-admin/', event_admin_site.urls),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

ADMIN_SITE_TITLE = "Superior4 - Admin"
ADMIN_SITE_HEADER = "Superior4"