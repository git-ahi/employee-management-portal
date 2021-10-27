from django.urls import path
from api import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('department', views.departmentsApi),
    path('department/[0-9+]', views.departmentsApi),
    path('employee', views.employeeApi),
    path('department/[0-9+]', views.employeeApi),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
