from django.db import models

# Create your models here.
class Sign_up(models.Model):
    u_id=models.AutoField(primary_key=True)
    F_name=models.CharField(max_length=255)
    L_name=models.CharField(max_length=255)
    Signup_U_name=models.CharField(max_length=255)
    pwd1=models.CharField(max_length=10)
    signup_email=models.CharField(max_length=100)
    contact=models.CharField(max_length=13)
    DOB=models.DateField()
    Status=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Signup: '+ self.F_name + self.L_name
    

class Cont_us(models.Model):
    Full_name=models.CharField(max_length=255)
    email_addr=models.CharField(max_length=100)
    ph_no=models.CharField(max_length=13)
    Content=models.TextField()
    timeStamp1=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from: '+ self.Full_name