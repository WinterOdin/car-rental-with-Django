from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Year(models.Model):
    name = models.CharField(max_length=4,unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    year_id    = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    time       = models.IntegerField(null=True,blank=True)
    about      = models.TextField(max_length=355,null=True, blank=True)
    shortAbout = models.CharField(max_length=70,null=True, blank=True)
    marka      = models.CharField(max_length=50,null=True, blank=True, default='Mercedes')
    model      = models.CharField(max_length=70,null=True, blank=True)
    topSpeed   = models.IntegerField(null=True,blank=True)
    nm         = models.IntegerField(null=True,blank=True)
    hp         = models.IntegerField(null=True,blank=True)
    seats      = models.IntegerField(null=True,blank=True)
    price      = models.CharField(max_length=10,null=True,blank=True)
    insurance  = models.IntegerField(null=True,blank=True)
    tank       = models.IntegerField(null=True,blank=True)
    car1       = models.ImageField(null=True)
    car2       = models.ImageField(null=True)
    car3       = models.ImageField(null=True)
    car4       = models.ImageField(null=True)
    car5       = models.ImageField(null=True)
    
    
    
    def __str__(self):
        return self.model


class Faq(models.Model):
    titlePrev = models.CharField(max_length=20, null=True)
    content   = models.TextField(max_length=375,null=True, blank=True)
    question  = models.CharField(max_length=60, null=True)

    def __str__(self):
	    return self.titlePrev

class Customer(models.Model):
    user            = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name            = models.CharField(max_length=50, null=True)
    phone           = models.CharField(max_length=12, null=True)
    email           = models.CharField(max_length=25, null=True)
    dateCreated     = models.DateTimeField(auto_now_add=True, null=True)
    profilePic      = models.ImageField(default="basicUser.jpg",null=True, blank=True)
   

    def __str__(self):
        return self.name




class Location(models.Model):
    pickUpPlace  = models.CharField(max_length=105, null=True)

    def __str__(self):
        return self.pickUpPlace 



class Additions(models.Model):
    name     = models.CharField(max_length=105, null=False)
    insurance = models.IntegerField(null=True,blank=True)
    fuel      = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name



class Order(models.Model):
   
    customer     = models.CharField(max_length=70,null=True)
    customerID   = models.CharField(max_length=50, null=True)
    carModel     = models.CharField(max_length=70,null=True)
    automobileId = models.CharField(null=True,max_length=10)
    price        = models.IntegerField(null=True,blank=False)
    startRent    = models.DateField(auto_now_add=False, null=True)
    endRent      = models.DateField(auto_now_add=False, null=True)
    orderDate    = models.DateTimeField(auto_now_add=True, null=True)
    pickUp       = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    fullFuel     = models.BooleanField(blank=True, null=True,default=False)
    insurance    = models.BooleanField(blank=True, null=True, default=False)
    payed        = models.BooleanField( null=True, default=False)

    def __int__(self):
        return self.id

class canceledOrders(models.Model):
    customerID   = models.CharField(max_length=50, null=True)
    automobileId = models.CharField(null=True,max_length=10)
    price        = models.IntegerField(null=True,blank=False)
    payed        = models.BooleanField( null=True, default=False)
   