from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_rest/', include('api_rest.urls'), name='api_rest_urls'),
    path('', include('holiday.urls'), name='holiday_urls'),
    path('auth/', include('user.urls'), name='auth_urls'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
