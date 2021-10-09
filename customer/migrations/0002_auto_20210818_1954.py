# Generated by Django 3.2.6 on 2021-08-18 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customization', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации лида'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='origin_category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_category', to='customization.origincategory', verbose_name='Источник лида'),
        ),
    ]
