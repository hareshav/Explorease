from django.db import models
# Create your models here.
class cab(models.Model):
    driver_name=models.CharField(max_length=100)
    Licence_no=models.CharField(max_length=15)
    insurance=models.CharField(max_length=100)
    vechile_no=models.IntegerField(null=True)
    rc_book_no=models.CharField(max_length=100)
    aadhar_no=models.IntegerField(null=True,default=0)
    phone_no1=models.IntegerField(null=True)
    phone_no2=models.IntegerField(null=True)
    carImage=models.CharField(max_length=100000,null=True)
    def __str__(self):
        return self.driver_name
class Hotels(models.Model):
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    image=models.CharField(max_length=100000,null=True)
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100,null=True)
    bussiness_registration=models.IntegerField(null=True)
    rating=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class places(models.Model):
    place_name=models.CharField(max_length=100)
    place_desc=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    image=models.CharField(max_length=100000,null=True)
    image1=models.CharField(max_length=1000000,null=True)
    image2=models.CharField(max_length=1000000,null=True)
    def __str__(self):
        return self.place_name
class lodge(models.Model):
    name=models.CharField(max_length=100)
    contacts=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    typeOfroom=models.CharField(max_length=100)
    total_rooms=models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.name
class food(models.Model):
    image=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    rating=models.FloatField()
    Location=models.CharField(max_length=1000)
    type=models.CharField(max_length=100,choices=(('veg','veg'),('Non-veg','Non-veg')))
    def __str__(self):
        return self.title

