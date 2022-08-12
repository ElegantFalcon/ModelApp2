from django.urls import path
from appl import views


urlpatterns = [
    path('', views.index, name = 'index') , 
    path('home' , views.home , name = 'home') , 
    path('login' , views.login , name = 'login'),
    path('first_api/' , views.firstApi , name ="first_api"),
    path('user_data', views.user_data , name = 'user_data'),
    path('pro_det' , views.pro_details , name = 'product_details' )
]