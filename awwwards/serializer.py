from rest_framework import serializers
from .models import AwwwardsCriteria

class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwwwardsCriteria
        fields = ('design', 'usability', 'content')