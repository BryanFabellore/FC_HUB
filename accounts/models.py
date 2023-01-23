from django.db import models

# Create your models here.

class user_acc(models.Model):
    #basic info that is needed
    fName = models.CharField(max_length=250)
    lName = models.CharField(max_length=250)
    usr_contact_num = models.IntegerField()
    usr_gender = models.CharField(max_length=250)
    usr_city = models.CharField(max_length=250)
    usr_barangay = models.CharField(max_length=250)
    usr_street = models.CharField(max_length=250)
    usr_email = models.EmailField(max_length=250)
    usr_zipcode = models.CharField(max_length=150)
    usr_province = models.CharField(max_length=250)
    
    #Account configs
    usr_username = models.CharField(max_length=250)
    usr_password = models.CharField(max_length=250)
   

    