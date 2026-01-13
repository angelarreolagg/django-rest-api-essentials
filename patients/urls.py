from django.urls import path
from patients.views import ListPatientsView 

urlpatterns = [
    path("patients/", ListPatientsView.as_view()),
    # path("patients/<str:pk>/", patient_detail),
]
