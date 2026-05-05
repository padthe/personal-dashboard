from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DashboardItem
from .serializers import DashboardItemSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def get_items(request):
    if request.method == 'GET':
        items = DashboardItem.objects.all()
        serializer = DashboardItemSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DashboardItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    return Response(serializer.error)
    