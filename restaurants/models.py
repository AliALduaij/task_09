from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)

    def __str__(self):
    	return self.name

class User(models.Model):
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)