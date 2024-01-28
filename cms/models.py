from django.db import models


# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_name = models.CharField(max_length=20, verbose_name='Имя')
    cms_age = models.CharField(max_length=20, verbose_name='Возраст')
    cms_description = models.CharField(max_length=20, verbose_name='Описание')

    def __str__(self):
        return self.cms_name

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайд'
