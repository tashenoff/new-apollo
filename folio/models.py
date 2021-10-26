from django.db import models


class Folio(models.Model):

    folio_name = models.CharField(max_length=100, verbose_name="Компания")
    folio_link = models.CharField(max_length=100, verbose_name="Ссылка")
    folio_image = models.FileField(blank = True,null = True,verbose_name="Загрузка обложки")
    

    def __str__(self):
        return self.folio_name

    class Meta:
        verbose_name_plural = 'Портфолио'
        verbose_name = 'Портфолио'
