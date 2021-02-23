from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from devtz import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', include("devs.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + \
    static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)