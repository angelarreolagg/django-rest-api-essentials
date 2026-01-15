from rest_framework import viewsets
from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    Get Medical Bookings - Notes that you can read in Swagger Documentation or Redoc
    """

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
