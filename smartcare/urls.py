from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact_us/',include("contact_us.urls")),
    path('service/',include("service.urls")),
    path('',include("patient.urls")),
    path('doctor/',include("doctor.urls")),
    path('appointment/',include("appointment.urls")),
]
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
