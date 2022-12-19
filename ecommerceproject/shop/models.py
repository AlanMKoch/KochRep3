from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='categoryimages',blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('shop:product_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    # eeth category de under il aanu ee product enn kaanikkan
    #ForeignKey-other table il olla field ee field il use cheyyan
                            #category  field aayit link ondakkum,on_delete-previous values delete cheyth ith varaan
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='productimages',blank=True)
    stock=models.IntegerField()
    #true or false statement il stock available aano enn kaanikkan
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shop:prodcatdetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)