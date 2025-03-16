from django.urls import path
from .views import home, about, menu, book, display_menu_items, menu_item_detail

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('book/', book, name='book'),
    path('menu_item/', display_menu_items, name='menu_item_list'),
    path('menu_item/<int:pk>/', menu_item_detail, name='menu_item_detail'),  
]
