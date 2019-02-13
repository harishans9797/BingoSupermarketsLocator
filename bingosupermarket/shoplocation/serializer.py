from rest_framework import serializers
from .models import ShopLocations
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopLocations
        fields = '__all__'