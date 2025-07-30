from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    # busquedas en el sitio web
    path('search/', views.ProductSearchListView.as_view(), name='search'),
    # pk hace referencia al campo id
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'),
]
