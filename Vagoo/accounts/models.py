from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import CASCADE


class Profile(models.Model):
    class Meta:
        verbose_name = 'نمایه کاربری'
        verbose_name_plural = 'نمایه کاربری'

    user = models.OneToOneField(User, on_delete=CASCADE, verbose_name='حساب کاربری/username')
    mobile = models.CharField('تلفن همراه/Mobile', max_length=11)
    MALE = 1
    FEMALE = 2
    OTHER = 3
    GENDER_CHOICES = {
        (MALE, 'مرد/Male'),
        (FEMALE, 'زن/Female'),
        (OTHER, 'سایر/Other'),
    }
    gender = models.IntegerField('جنسیت/Gender', choices=GENDER_CHOICES)
    birth_date = models.DateTimeField('تاریخ تولد/Birth date', null=True, blank=True)
    country = models.CharField('کشور/County', max_length=100, null=True, blank=True)
    city = models.CharField('شهر/City', max_length=100, null=True, blank=True)
    profile_image = models.ImageField('تصویر/Image', upload_to='users/profile_images', null=True, blank=True)
    balance = models.PositiveIntegerField('اعتبار/Credit', default=0)

    def __str__(self):
        return self.user.get_full_name()

    def get_balance(self):
        return '{} تومان'.format(self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def spend(self, amount):
        if self.balance > amount:
            self.balance -= amount
            self.save()
            return True
        else:
            return False
