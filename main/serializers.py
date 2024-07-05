from rest_framework import serializers

from .models import Construction, Organization, Building


class ConstructionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = '__all__'


class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class BuildingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'