from django.urls import path
from . import views

urlpatterns= [
	path("",views.main_view),
	path('result/',views.result),
]