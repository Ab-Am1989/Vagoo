# Generated by Django 3.2.8 on 2022-02-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(2, 'زن/Female'), (3, 'سایر/Other'), (1, 'مرد/Male')], null=True, verbose_name='جنسیت/Gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='تلفن همراه/Mobile'),
        ),
    ]
