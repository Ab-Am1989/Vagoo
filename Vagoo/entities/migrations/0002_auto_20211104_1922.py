# Generated by Django 3.2.8 on 2021-11-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journeyimages',
            options={'verbose_name': 'عکس سفر', 'verbose_name_plural': 'عکس سفر'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': 'ترانه', 'verbose_name_plural': 'ترانه'},
        ),
        migrations.AddField(
            model_name='journeyimages',
            name='default',
            field=models.BooleanField(default=False, verbose_name='تصویر پیش\u200cفرض'),
        ),
        migrations.AlterField(
            model_name='journeyimages',
            name='image',
            field=models.ImageField(upload_to='upload_to_gallery'),
        ),
    ]
