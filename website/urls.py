from django.urls import path
from . import views, utilitiesViews
from graph import views as graph



urlpatterns = [
	path('', views.home, name='home'),
	path('loadForm/', views.loadForm, name='ajax_load'),
    path('infoGenerated/', views.loadData, name='infoGenerated'),
	path('carinfo/<str:pk>/',views.carPage, name='carPage'),
	path('gallery',views.gallery, name='gallery'),


	path('register/', views.registerPage, name='register'),
	path('logout/',views.logoutPage, name='logout'),
	path('customer/<str:pk>/',views.customerPage, name='customer'),
	path('updateView/',views.updateView, name='updateView'),
	


	path('createOrder/<str:pk>/',views.createOrder, name='createOrder'),
	path('makeOrder/<str:pk>/',views.makeOrder, name='makeOrder'),
	path('payment/<str:pk>/', views.payment, name='payment'),
	path('cancelOrder/<str:pk>/', views.cancelOrder, name='cancelOrder'),


	path('pdfView/<str:pk>/', utilitiesViews.ViewPDF.as_view(), name="pdfView"),
    path('pdfDownload/<str:pk>/', utilitiesViews.DownloadPDF.as_view(), name="pdfDownload"),
	
	path('graph', graph.graph, name="graph"),

]
