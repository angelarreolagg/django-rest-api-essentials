from django.urls import path
from patients.views import patient_list, patient_detail

urlpatterns = [
    path("patients/", patient_list),
    path("patients/<str:pk>/", patient_detail),
]
