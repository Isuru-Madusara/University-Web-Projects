from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category_view, name='categories'),
    path('unit/', views.unit_view, name='units'),
    path('item/', views.item_view, name='items'),
    path('supplier/', views.supplier_view, name='suppliers'),
    path('order/', views.order_view, name='orders'),
    path('employee/', views.employee_view, name='employees'),
    path('', views.home, name="home"),
    path('item/view/<int:id>/', views.item_detail, name='item_detail'),
    
]