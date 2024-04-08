from rest_framework import serializers
from .models import ServiceRequest

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['id', 'status', 'request_type', 'details', 'attachment', 'date_submitted', 'date_resolved']
