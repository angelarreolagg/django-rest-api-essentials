from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @action(["GET"], detail=True, url_path="clinical-history")
    def clinical_history(self, request, pk=None):
        """
        Returns the patient's medical record report in JSON format.
        Includes personal data, medical history, insurance information, and clinical records.
        """
        patient = self.get_object()
        insurances = patient.insurances.all().values(
            "provider", "policy_number", "expiration_date"
        )
        records = patient.medical_records.all().values(
            "date", "diagnosis", "treatment", "follow_up_date"
        )

        report = {
            "patient": {
                "id": patient.id,
                "full_name": f"{patient.first_name} {patient.last_name}",
                "date_of_birth": patient.date_of_birth,
                "contact_number": patient.contact_number,
                "email": patient.email,
                "address": patient.address,
                "medical_history": patient.medical_history,
            },
            "insurances": list(insurances),
            "medical_records": list(records),
        }
        return Response(report)
