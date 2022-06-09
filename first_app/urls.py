from django.urls import path
from .views import hellodjango, date_hw, date_year, date_month, date_day, func_name

urlpatterns = [
    path('', hellodjango),
    path('func_name/<str:name>/', func_name),
    path('date/', date_hw),
    path('date/year/', date_year),
    path('date/day/', date_day),
    path('date/month/', date_month)
]
