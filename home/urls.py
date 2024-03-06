from django.urls import path
from .views import *


urlpatterns = [
    path('', UserView.as_view()),
    path('user<int:pk>/', UserRetriveView.as_view(), name='user-pk'),
]