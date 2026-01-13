from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'bookings', views.AppointmentViewSet, basename='bookings')
router.register(r'medical_note', views.MedicalNoteViewSet, basename='medical_note')
urlpatterns = router.urls
