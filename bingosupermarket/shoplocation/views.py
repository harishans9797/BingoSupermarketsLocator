from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import ShopLocations
from .serializer import ShopSerializer
from rest_framework import generics
from rest_framework.generics import (DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView)
from django.shortcuts import render



class ShopList(generics.ListCreateAPIView):
    queryset = ShopLocations.objects.all()
    serializer_class = ShopSerializer

    def filter_queryset(self, queryset):
        queryset = super(ShopList, self).filter_queryset(queryset)
        return queryset.order_by('-distance').reverse()




