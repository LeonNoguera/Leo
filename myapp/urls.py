
from django.urls import path
from .views import LoginViw,InfoView,Logout,FormView

urlpatterns=[
    path('', LoginViw.as_view(),name='login'),
    path('logout/', Logout.as_view(),name='logout'),
    
    
    path('info', InfoView.as_view(),name='info'),
    path('formulario', FormView.as_view(),name='form'),

]