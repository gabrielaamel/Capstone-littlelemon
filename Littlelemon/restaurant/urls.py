from django.urls import path
from . import views
#from django.conf.urls.static import static
#from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('menu/items/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    
]