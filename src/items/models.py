from django.db import models

# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    image = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = './static' + self.image.url
        except:
            url = ''
        return url
    
    @property
    def get_delete_url(self):
        return f"/delete/{self.id}/"

    @property
    def get_sell_url(self):
        return f"/sell/{self.id}/"

class Money(models.Model):
    total = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    discount = models.IntegerField(default=0)
