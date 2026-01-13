from django.urls import path
from doctors.views import DoctorList, DoctorDetail

urlpatterns = [
    path("doctors/", DoctorList.as_view()),
    path("doctors/<str:pk>/", DoctorDetail.as_view()),
]
