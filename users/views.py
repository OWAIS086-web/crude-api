from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class UserProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])    
class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])  
class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
@authentication_classes([TokenAuthentication]) 
@permission_classes([IsAuthenticated])
class UserProfileDeleteView(generics.DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    

""""
1. import the generic from rest_framework  which provide interface
   import the  userprofile and serializers  

2. create API view from generics ( Retrieve, Create,  Update, Delete)   

3. queryset  to add all the value of UserProfile table

4. serializer_class can responeable to send data in json form

5. decorators  is use to make sure only authorized person can use it  
"""