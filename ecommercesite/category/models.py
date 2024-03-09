from django.db import models

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length = 150)
  slug = models.SlugField(max_length = 150 , unique = True)
  description = models.CharField(max_length = 150, blank = True)
  car_image = models.ImageField(upload_to="photos/categories",blank =  True)

  class Meta:
    verbose_name = 'category'
    verbose_name_plural = 'categories'


  def __str__(self):
    return self.category_name