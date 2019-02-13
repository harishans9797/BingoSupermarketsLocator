from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from shoplocation import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', views.ShopList.as_view(), name="getpostbingolocations"),


]

urlpatterns = format_suffix_patterns(urlpatterns)
