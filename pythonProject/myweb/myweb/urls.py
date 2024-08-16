
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('base.urls')),
    path('api/', include('base.api.urls'))
=======
    path('app/', include('base.urls')),
    path('about/', include('base.urls')),
    path('contact/', include('base.urls')),
    path('login/', include('base.urls'))
>>>>>>> origin/main

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)