# Generated by Django 2.2.13 on 2020-07-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200728_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text_full',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Текст_Полный'),
        ),
    ]
