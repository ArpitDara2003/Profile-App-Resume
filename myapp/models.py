from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skill(models.Model):  # Inherit from models.Model
    skill_username = models.CharField(max_length=255,default ='Robot')
    skill_name = models.CharField(max_length=255,default="")
    skill_discription = models.CharField(max_length=255,default="")
    detailed_discription = models.CharField(max_length=6000,default="")
    point1 = models.CharField(max_length=255,default="")
    point2 = models.CharField(max_length=255,default="")
    point3 = models.CharField(max_length=255,default="")
    point4 = models.CharField(max_length=255,default="")
    point5 = models.CharField(max_length=255,default="")
    highlighted = models.BooleanField(default=True)

class Certificate(models.Model):
    certificate_username = models.CharField(max_length=255,default ='Robot')
    certificate_name = models.CharField(max_length=255)
    certificate_image = models.ImageField(upload_to='static/certificates', default='static/images/img1.png')
    short_discription = models.CharField(max_length=255,default="")
    detailed_discription = models.CharField(max_length=6000,default="")


class Creater(models.Model):
    user_id = models.CharField(max_length=255, default='Robot')
    discription = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to='static/images', default='static/certificates/Robot.png')
    full_name = models.CharField(max_length=255, default="")
    detailed_discription = models.CharField(max_length=1000, default="")
    date_of_birth = models.CharField(max_length=15, default="")
    address = models.CharField(max_length=255, default="")
    linkedin = models.CharField(max_length=255, default="")
    instagram = models.CharField(max_length=255, default="")
    facebook = models.CharField(max_length=255, default="")
    contact_no = models.CharField(max_length=15, default="")
    



