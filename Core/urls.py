
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import set_language



urlpatterns = i18n_patterns(
    path('admin', admin.site.urls),
    path('f/', include('recognition.urls')),  # Ilovamiz URL-lari
    path('', include('app1.urls')),
    path('set-language/', set_language, name='set_language'), # Tilni o'zgartirish
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
