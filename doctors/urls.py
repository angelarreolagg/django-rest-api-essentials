from django.urls import path
from doctors.views import doctor_list, doctor_detail

urlpatterns = [
    path("doctors/", doctor_list),
    path("doctors/<str:pk>/", doctor_detail),
]
