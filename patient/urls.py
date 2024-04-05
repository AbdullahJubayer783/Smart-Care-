from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('list', views.PatientViewsets)


urlpatterns = [
    path('',include(router.urls)),
    # path('list/',views.PatientViewsets.as_view(),name="patient"),
    # path('list/<int:id>/',views.PatientViewsets.as_view(),name="patientid"),
    path('register/',views.RegistrationAPIView.as_view(), name='register'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('logout/',views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
] 
