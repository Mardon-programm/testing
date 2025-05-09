from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.yasg import urlpatterns_yasg
from app.users import urls

# Основные маршруты (не зависят от мультиязычности)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(urlpatterns_yasg)),  # ✅ Swagger (yasg)
]

# Маршруты, зависящие от языка (i18n)
urlpatterns += i18n_patterns(
    #path('api/v1/ваше приложение/', include('app.ваше приложение.urls')),
    path('api/v1/users/', include('app.users.urls')),
)

# Раздача статических и медиа-файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)