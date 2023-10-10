from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100)  
    slug = models.SlugField(max_length=200,blank=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name
    

class Quantity(models.Model):
    variant_name = models.CharField (max_length=100)
    def __str__(self):
        return self.variant_name 
    

    

class Color(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    def __str__(self):
        return self.color_name

class Size(models.Model):
    size  = models.CharField(max_length=100)

    def __str__(self):
        return self.size
    
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/products')
    price = models.CharField(max_length=50)
    description = models.TextField()
    stock =models.IntegerField(default=100)

    quantity = models.ForeignKey(Quantity,blank=True,null=True,on_delete=models.CASCADE)
    sizes = models.ManyToManyField(Size, blank=True)
    color = models.ForeignKey(Color,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name




class ProductImages(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='static/products',default=1)

