from django.db import models

# Create your models here.


class Order(models.Model):
    order_form_dt = models.DateTimeField(auto_now=True)
    order_name_surname = models.CharField(max_length=200)
    order_age = models.CharField(max_length=100)
    order_location = models.CharField(max_length=200)
    order_circumstances = models.CharField(max_length=200)
    order_additional_info = models.CharField(max_length=200)

    def __str__(self):
        return self.order_name_surname

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'