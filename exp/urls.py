from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('api1/',views.viewcab.as_view(),name='api1'),
    path('api2/',views.viewplace.as_view(),name='api2'),
    path('api3/',views.viewhotel.as_view(),name='api3'),
    path('api4/',views.viewlodge.as_view(),name='api4'),
]