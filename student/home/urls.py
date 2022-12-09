from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home.as_view(),name='home'),
    path('enquery/', views.Enquery.as_view(),name='enquery'),
    
]