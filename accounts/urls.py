from django.urls import path, include
from rest_framework import routers
 
from .views import SignUpView, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
 
urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),

]