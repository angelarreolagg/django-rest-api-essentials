from datetime import date
import re
from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from bookings.serializers import AppointmentSerializer


class DoctorSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    years_of_experience = serializers.SerializerMethodField()
    class Meta:
        model = Doctor
        fields = [
            "first_name",
            "last_name",
            "qualification",
            "contact_number",
            "email",
            "address",
            "start_date",
            "years_of_experience",
            "biography",
            "is_on_vacation",
            "appointments",
        ]
    
    def get_years_of_experience(self, obj):
        if obj.start_date != None:
            return (date.today() - obj.start_date).days // 365
        return "Not available"

    def validate_email(self, value):
       # Regex pattern: valid email format with @example.com domain
        email_regex = r'^[a-zA-Z0-9._%+-]+@example\.com$'
        if not re.match(email_regex, value):
            return value
        raise serializers.ValidationError("Email must be in the format: username@example.com")

    def validate(self, attrs):
        if len(attrs["contact_number"]) < 11 and attrs["is_on_vacation"] == True:
            raise serializers.ValidationError(
                "Please update the contact information with a valid phone number before setting the doctor on vacation."
            )
        return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = "__all__"


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = "__all__"
