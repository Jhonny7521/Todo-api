from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('pagos.urls')),
]
