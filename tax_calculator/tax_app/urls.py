from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.default_view),
    path('<int:number/>' , views.calculate_tax),
    path('taxrate/',views.show_tax_rate),
]
