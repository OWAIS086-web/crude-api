from django.urls import path
from .views import UserProfileListView, UserProfileCreateView, UserProfileUpdateView, UserProfileDeleteView

urlpatterns = [
    path('users/', UserProfileListView.as_view(), name='userprofile-list'),
    path('create/', UserProfileCreateView.as_view(), name='userprofile-create'),
    path('update/<int:pk>/', UserProfileUpdateView.as_view(), name='update-user-profile'),
    path('delete/<int:pk>/', UserProfileDeleteView.as_view(), name='delete-user-profile'),
]


""""
1. import all over view from users.views    

2. create urls  mapping pattren url name and which function is call on it   

"""