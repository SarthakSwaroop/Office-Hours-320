from rest_framework import serializers
from .models import StudentAvailability, StudentSchedule, ProfessorOptions, StudentRankings, Login

class StudentAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAvailability
        fields = '__all__'

class StudentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSchedule
        fields = '__all__'

class ProfessorOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorOptions
        fields = '__all__'

class StudentRankingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRankings
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'