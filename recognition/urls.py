from django.urls import path
from . import views

app_name = 'recognition'

urlpatterns = [
    path('', views.camera_view , name='take_video'),
    path('vid/', views.get_video, name='get_video'),
    path('add/', views.add_data, name='add_data'),
]