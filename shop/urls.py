from . import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:id>/', views.shop_detail, name='detail')
]
