from django.urls import path
from api import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('depertment', views.depertmentApi),
    path('depertment/[0-9-]', views.depertmentApi),
    path('employee', views.employeeApi),
    path('depertment/[0-9+]', views.employeeApi),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

