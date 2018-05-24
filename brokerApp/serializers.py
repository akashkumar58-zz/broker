from rest_framework import serializers
from .models import ServiceRecord

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRecord
        fields = ('service_id', 'plan_id', 'organization_guid', 'space_guid')
