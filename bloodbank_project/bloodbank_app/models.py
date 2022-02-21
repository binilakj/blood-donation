from django.db import models

# Create your models here.
class Blood_Bank(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='photo')
    des = models.TextField()

    def __str__(self):
        return self.name

class Districts(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='district'
        verbose_name_plural='districts'

    def __str__(self):
        return '{}'.format(self.name)

class Centers(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    category=models.ForeignKey(Districts,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'center'
        verbose_name_plural = 'centers'

    def __str__(self):
        return '{}'.format(self.name)