from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('form', views.BiodataViews, name= 'form'),
    path('e_form', views.EmploymentDetails, name= 'e_form')

]



