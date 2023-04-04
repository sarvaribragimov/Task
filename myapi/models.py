# Create your models here.
import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    STATUS = (
        ('student','student'),
        ('teacher','teacher'),
        ('admin','admin'),
        ('super-admin','super-admin'),
    )
    image = models.ImageField(upload_to='image')
    status = models.CharField(max_length=50,choices=STATUS)
class Group(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = ("Guruh")
        verbose_name_plural = ("Guruhlar")
    def __str__(self):
        return self.name

class Student(models.Model):
    fish = models.CharField(max_length=100)
    date = models.DateTimeField()
    parent_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,null=False)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
   
 
    def __str__(self):
        return self.fish
    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Studentlar")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)    

class Organization_name(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Organization_name")
        verbose_name_plural = ("Organization_name")
    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Level")
        verbose_name_plural = ("Level")
    def __str__(self):
        return self.name

class Organization_address(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Organization_address")
        verbose_name_plural = ("Organization_address")
    def __str__(self):
        return self.name

class Student_information(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    image = models.ImageField(upload_to="image")
    birth_date = models.DateTimeField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=200)
    user_parol = models.IntegerField()
    user_login = models.CharField(max_length=60)
    parents_name = models.CharField(max_length=100)
    parents_phone_number = models.IntegerField()

    muassasa_nomi = models.ForeignKey(Organization_name,on_delete=models.CASCADE)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    muassasa_manzili = models.ForeignKey(Organization_address,on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("student")
        verbose_name_plural = ("students")

    def __str__(self):
        return self.first_name



 
