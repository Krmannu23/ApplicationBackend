
from django.db import models
class Identity(models.Model):
    first_name=models.CharField(max_length=40,null=True,blank=False)
    last_name=models.CharField(max_length=40,null=True,blank=False)
    def __str__ (self):
        return self.first_name
