from django.urls import path,include
from rest_framework import routers
from .views import RegisterUserAPIView,StudentListApiview,LoginView,StudentViewSet,LogoutAPIView,login_api,register_api

router = routers.DefaultRouter()
router.register(r'',StudentViewSet)


urlpatterns = [  
  path('register/',RegisterUserAPIView.as_view()),
  path('login/',LoginView.as_view()),
  path('logout/', LogoutAPIView.as_view(), name='logout'),
  path('',StudentListApiview.as_view(),name="StudentListApiview"),
  path('crud/',include(router.urls)),
  path('registerapi/',register_api,name="registerapi"),
  path('loginapi/',login_api,name="loginapi"),
  
]



