from django.db import models

# Create your models here.

class Nutrient(models.Model):
  name = models.CharField(max_length=256)
  def __str__(self):
    return self.name

class Meal(models.Model):
  name = models.CharField(max_length=256)
  date_added = models.DateTimeField('Date Added')
  nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Dish(models.Model):
  suggested_time = models.DateTimeField('Suggested Time')
  time_served = models.DateTimeField('Time Served', blank=True, null=True)
  meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
