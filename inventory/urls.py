from django.urls import  path
from .views import  (Home_Page,
                     issue_item, add_to_stock, Search_Product, Reciept_Views, Total_Sales, Add_Product, Product_Detail, Reciept_Detail )
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home_Page.as_view(), name = "home"),
    path('search', Search_Product.as_view(), name = "search"),
    path('receipt/', Reciept_Views.as_view(), name = "receipt"),
    path('new_product', Add_Product.as_view(), name = "new_product"),
    path('receipt/<int:pk>/', Reciept_Detail.as_view(), name='receipt_detail'),
    path('home/<int:pk>/', Product_Detail.as_view(), name='product_detail'),
    path('issue_item/<str:pk>/', issue_item, name='issue_item'),   
    path('add_to_stock/<str:pk>/', add_to_stock, name='add_to_stock'),
    path('all_sales/', Total_Sales.as_view(), name = 'all_sales')

]