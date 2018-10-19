from django.urls import path
from . import views

urlpatterns= [
	path("",views.main_view),
	#path('result/',views.result),
	path('allAccounts/',views.allAccounts),
	path('resultallAccounts/',views.resultallAccounts),
	path('transfer/',views.transfer),
	path('resultTransfer/',views.resultTransfer),
]