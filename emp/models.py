from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator  
# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.testimonial
     

