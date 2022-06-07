from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main import settings
from main.views import Home

urlpatterns = [
                  path('', Home.as_view(), name="home"),
                  path('admin/', admin.site.urls),
                  path('account/', include('accounts.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
