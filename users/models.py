from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(_("City"),max_length=255)
    cnic = models.CharField(_("CNIC"),max_length=15,unique=True)
    address = models.TextField(_("Address"))

    def __str__(self):
        return self.user.username
    


""""
1. for user i use Django auth User because we cannot need  to define custom user for this  task  

2. create a model name UserProfile as mention is test point 3  

3. define field as mention 

4. using gettext_lazy define defualt placeholder value 
"""

