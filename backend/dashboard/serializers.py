from rest_framework import serializers
from .models import DashboardItem


class DashboardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardItem
        fields = '__all__'