from django.db import models

# Create your models here.
from django.urls import reverse


class Animal(models.Model):
    """
    Let's use model so we can add some additional info to our users later
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Color(models.Model):
    """
    Same as animal, why not?
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Respondent(models.Model):
    """
    Every block represents respondent form
    """
    # first block
    first_name = models.CharField(max_length=20, )
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    # second block
    profile_photo = models.ImageField(upload_to='app/photos')
    hair_color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    weight = models.PositiveSmallIntegerField()
    # third block
    favorite_animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    has_pet = models.BooleanField()

    def get_absolute_url(self):
        return reverse('view_respondent', args=[self.id])
