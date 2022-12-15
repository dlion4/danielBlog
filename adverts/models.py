from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.



    
    
class Advert(models.Model):
    name = models.CharField(max_length=100, verbose_name="Advert Name")
    source = models.CharField(max_length=100, verbose_name="Advert Source")
    url = models.URLField(verbose_name="Advert Url", max_length=255, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    descr = models.CharField(max_length=200, verbose_name="Advert Description", blank=True, null=True)
    

    class Meta:
        verbose_name = _("Advert")
        verbose_name_plural = _("Adverts")

    def __str__(self):
        return self.name
    

class AdvertImage(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name="advert_image")
    image = models.ImageField(upload_to="adverts/", blank=True, null=True)
    
    def __str__(self):
        return f"{self.advert.name} Image"
