from cloudinary.models import CloudinaryField
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class ReadyToPress(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()    
    image = CloudinaryField('product_images/')
    smprice = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    mdprice = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    lgprice = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    xlprice = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    xxlprice = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CustomDesign(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    def __str__(self):
        return f"{self.title} - {self.price}"

class CustomDesignPhoto(models.Model):
    custom_design = models.ForeignKey(CustomDesign, related_name='photos', on_delete=models.CASCADE)
    photo = CloudinaryField('product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.custom_design.title} - {self.custom_design.price} Photo"