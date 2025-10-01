from django.contrib import admin
from django.urls import path
from ssr_inMemory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('drug/<int:drug_id>/', views.drug_detail, name='drug_detail'),  # Правильно: drug_id
    path('cart/', views.cart, name='cart'),
]