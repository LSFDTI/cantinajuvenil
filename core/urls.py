from django.urls import path, include
from .views import home, campistas

urlpatterns = [

	path('',home, name = 'core_home'),
	path('campistas/',campistas, name = 'core_campistas')
  
 ]

