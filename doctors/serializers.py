import re
from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

    def validate_email(self, value):
       # Regex pattern: valid email format with @example.com domain
        email_regex = r'^[a-zA-Z0-9._%+-]+@example\.com$'
        if not re.match(email_regex, value):
            return value
        raise serializers.ValidationError("Email must be in the format: username@example.com")

    def validate(self, attrs):
        if len(attrs["contact_number"]) < 10 and attrs["is_on_vacation"] == True:
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
