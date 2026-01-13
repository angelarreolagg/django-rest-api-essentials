from django.urls import path
from patients.views import PatientList, PatientDetail

urlpatterns = [
    path("patients/", PatientList.as_view()),
    path("patients/<str:pk>/", PatientDetail.as_view()),
]