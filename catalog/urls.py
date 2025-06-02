from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('catalog/create', ProductCreateView.as_view(), name='products_create'),
    path('catalog/update/<int:pk>/', ProductUpdateView.as_view(), name='products_update'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('catalog/delete/<int:pk>/', ProductDeleteView.as_view(), name='products_delete'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]