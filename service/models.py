from django.db import models

# Create your models here.
class Service(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to="service/images/")
    class Meta:
        verbose_name_plural = "Service"