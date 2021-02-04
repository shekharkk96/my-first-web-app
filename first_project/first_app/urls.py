from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.secondPage_data,name="secondPage"),
]
