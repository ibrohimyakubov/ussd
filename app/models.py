from ckeditor.fields import RichTextField
from django.db import models
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Company(models.Model):
    COMPANY = [
        ('Ucell', 'ucell'),
        ('Beeline', 'beeline'),
        ('MobiUz', 'mobiuz'),
        ('Uzmobile', 'uzmobile'),
    ]
    title = models.CharField(choices=COMPANY, max_length=20)
    image = models.ImageField(upload_to='company/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kompaniya"

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


class Internet(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=56, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name_plural = "Internet"

    def __str__(self):
        return self.title


class I_Paket(models.Model):
    internet = models.ForeignKey(Internet, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    nomi = models.CharField(max_length=200, blank=False)
    hajmi = models.IntegerField()
    narxi = models.FloatField()
    haqida = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "Internetlar"


class Tariflar(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=56, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tarif"


class T_Paket(models.Model):
    tariflar = models.ForeignKey(Tariflar, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    nomi = models.CharField(max_length=200, blank=False)
    muddati = models.IntegerField()
    narxi = models.FloatField()
    haqida = RichTextField()

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "Tariflar"


class Daqiqalar(models.Model):
    title = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Daqiqa"


class D_Paket(models.Model):
    daqiqa = models.ForeignKey(Daqiqalar, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=200, blank=False)
    muddati = models.IntegerField()
    narxi = models.FloatField()
    haqida = RichTextField()

    class Meta:
        verbose_name_plural = "Daqiqalar"

    def __str__(self):
        return self.nomi


class SMS(models.Model):
    title = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "SMS"


class SMS_Paket(models.Model):
    sms = models.ForeignKey(SMS, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=200, blank=False)
    muddati = models.IntegerField()
    narxi = models.FloatField()
    haqida = RichTextField()

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "SMSlar"


class Foydali(models.Model):
    title = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Foyda"


class F_Paket(models.Model):
    foydali = models.ForeignKey(Foydali, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=200, blank=False)
    haqida = RichTextField()

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "Foydali"


class Xizmatlar(models.Model):
    title = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Xizmat"


class X_Paket(models.Model):
    xizmat = models.ForeignKey(Xizmatlar, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=200, blank=False)
    haqida = RichTextField()

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name_plural = "Xizmatlar"
