from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientSerializer
from .models import Patient


@api_view(["GET", "POST"])
def patient_list(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","DELETE"])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)