from rest_framework import serializers
from .models import Contact


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'phone',
            'email',
            'subject',
            'description',
        )
        model = Contact
