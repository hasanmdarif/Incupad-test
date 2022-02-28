from django.conf.urls import url
from django.contrib import admin
from .views import *
from .models import *
from django.urls import path
urlpatterns = [
    path('list/', StudentListView.as_view()),
    path('marks/', MarkListView.as_view()),
    path('list/<int:pk>/', StudentDetailView.as_view()),
    path('marks/<int:pk>/', MarkDetailView.as_view()),
]
