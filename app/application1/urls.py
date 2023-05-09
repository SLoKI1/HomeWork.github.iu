from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('Look/',views.HTLook, name='HTLook'),
    path('AddT/',views.HTAddT, name='HTAddT'),
    path('AddH/',views.HTAddH, name='HTAddH'),

    path('<int:pk>/h', views.BLANCHEADMAN.as_view(),name='BLANCHEADMAN'),
    path('<int:pk>/h/delet', views.DELETHEADMAN.as_view(),name='DELETHEADMAN'),

    path('<int:pk>/t', views.BLANCTEACHER.as_view(), name='BLANCTEACHER'),
    path('<int:pk>/t/delet', views.DELETTEACHER.as_view(), name='DELETTEACHER'),

]





