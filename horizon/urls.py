
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('',include('home.urls'),name='homepage'),
    path('admin/', admin.site.urls),
    path('mfa/',include('mfaauth.urls'),name='mfa'),
    path('services/',include('services.urls'),name='services'),
    path('admin/mfaauth/mfasecret/add/', RedirectView.as_view(url='/mfa/upload-mfa/', permanent=True)),    
    path("ckeditor/", include('ckeditor_uploader.urls')), # <-- here

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)