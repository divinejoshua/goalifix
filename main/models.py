from django.db import models

# Create your models here.

def upload_location(instance, filename):
	file_path = 'goalifix/{image}'.format(image=filename)
	return file_path


# Create your models here.
class Products(models.Model):
	brand        = models.CharField(max_length=100)
	device        = models.CharField(max_length=100)
	price        = models.PositiveIntegerField(blank=True)
	bidPrice     = models.PositiveIntegerField(blank=True, default=0)
	body         = models.TextField()
	date         = models.DateTimeField(auto_now_add=True)
	thumb        = models.ImageField(upload_to=upload_location, blank=True)

	def __str__(self):
		return self.device



# Create your models here.
class Bidder(models.Model):
	name        = models.CharField(max_length=100)
	email        = models.CharField(max_length=100)
	phone        = models.CharField(max_length=100)
	product 	 = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
	price        = models.PositiveIntegerField(blank=True)
	date         = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


# Create your models here.
class BidStatus(models.Model):
	active_bid				= models.BooleanField(default=False)
	date         = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.active_bid)