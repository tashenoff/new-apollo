from django.db import models
# from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from customer.models import Customer
from service.models import MainService
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.http import Http404
from django.conf import settings
# Create your models here.

# FirstName
# phone
# email
# company
# дата автоматическая
# нужно добавить сигнал, если была добавлена заявка
# default=lambda: OriginCategory.objects.get(id=1),

class Main(models.Model):

    status_choice = (
        (1, 'В обработке'),
        (2, 'На рассмотрении'),
        (3, 'Отменен'),
        (4, 'Завершен'),
        
    )
    status = models.PositiveSmallIntegerField(choices=status_choice,blank=True, null=True, default=status_choice[0][0], verbose_name="Статус заявки" )
    read = models.BooleanField(verbose_name="Отметить как прочитанное", default=False)
    сustomer = models.ForeignKey('customer.Customer', null=True, default=None, on_delete=models.CASCADE, related_name="main_customer", verbose_name="Клиент")
    comment = models.TextField(verbose_name="Дополнительный комментарий", max_length=255, blank=True, null=True)
    rec_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")
    meeting_date = models.DateField(blank=True, null=True, verbose_name="Дата встречи")
    main_service = models.ForeignKey('service.MainService', null=True, default=None, on_delete=models.CASCADE, related_name="main_service", verbose_name="Услуга")

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'

@receiver(post_save, sender=Main)
def send_email_new_order(sender, instance, created, **kwargs):

    # if a new officer is created, compose and send the email
    if created:
        name = instance.сustomer.firstName
        phone = instance.сustomer.phone
        service = instance.main_service.main_service_name

        subject = 'Новый заказа с сайта apollo --- Имя: {0}, Номер телефона: {1}, Услуга: {2}'.format(name, phone, service)
        message = 'Новый заказ\n'
        message += 'Имя: ' + name + '\n' + 'Номер телефона: ' + phone + '\n'+ 'Услуга:'+ service +'\n'
        message += '--' * 30

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            settings.RECIPIENTS_EMAIL,
            fail_silently=False,
        )
        
