from django.db import models

# Create your models here.
class INFORMATION(models.Model):
    Name=models.CharField(max_length=250)
    Remarks=models.CharField(max_length=600)
        
    def __str__(self):
        return self.Name
        
        