from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_index'),
    path('tables/', views.tables, name='admin_tables'),
    path('icon-menu/', views.icon_menu, name='admin_icon_menu'),
    path('login/', views.login, name='admin_login'),
    path('logout/', views.logout, name='admin_logout'),
    path('sidebar/', views.sidebar, name='admin_sidebar_style_2'),
    path('widgets/', views.widgets, name='admin_widgets'),
    path('starter-template/', views.starter_template, name='admin_starter_template'),
    path('datatables/', views.datatables, name='admin_datatables'),
    path('api/get-site-data/', views.get_site_data, name='get_site_data'),
]
