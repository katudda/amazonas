from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.catalogs.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('api/v1/', include('apps.api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)