from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Shop(models.Model):
    name = models.CharField(_("نام"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=200)
    price = models.IntegerField(_("قیمت"))
    photo = models.ImageField(
        _("عکس"), upload_to='shop/')

    def __str__(self):
        return self.name


class Detail(models.Model):
    c = [('blu', 'blu'), ('red', 'red'), ('with', 'with'), ('blacj', 'blacj')]
    s = [('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('XS', 'XS')]
    size = models.CharField(_("سایز"), max_length=50, choices=s)
    color = models.CharField(_(""), max_length=50, choices=c)
    

    def __str__(self):
        self.color
