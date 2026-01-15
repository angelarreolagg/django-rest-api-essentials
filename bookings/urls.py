from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r"bookings", viewsets.AppointmentViewSet, basename="bookings")
router.register(r"medical_note", viewsets.MedicalNoteViewSet, basename="medical_note")
urlpatterns = router.urls
