from django.urls import path, include
from . import views
from recognition.views import camera_view

app_name = 'app1'

urlpatterns = [
    path('', camera_view , name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]