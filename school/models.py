from django.db import models

# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=False)
    contact_email = models.EmailField(max_length=100, null=False)
    contact_number = models.CharField(max_length=13, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

def __str__(self):
        return self.name