from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class PostPet(models.Model):

    Male = 'M'
    Female = 'F'
    Unspecified = 'O'

    PET_GENDER = [
        (Male,'Male'),
        (Female, 'Female'),
        (Unspecified, 'Unspecified')
    ]

    pet=models.CharField(max_length=50)
    pet_name=models.CharField(max_length=50)
    pet_gender = models.CharField(max_length=1, choices=PET_GENDER)
    pet_breed=models.CharField(max_length=50)
    pet_color=models.CharField(max_length=50)
    pet_detail=models.TextField(max_length=500)
    pet_DOB=models.DateField(auto_now=False)
    poster=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.pet_name
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})
    