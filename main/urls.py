from django.urls import path, include

from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home_view, name="index"),
    path('home/', views.home_inner_view, name="home"),
    path('phones/', views.phone_view, name="phones"),
    path('laptops/', views.laptop_view, name="laptops"),
    path('accessories/', views.accessories_view, name="accessories"),
    path('bid/', views.bid_view, name="bid"),
    path('add-bid/', views.add_bid_view, name="addbid"),
]