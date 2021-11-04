# Generated by Django 3.2.8 on 2021-11-04 18:41

from django.db import migrations, models
import django.db.models.deletion
import entities.models
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام کتاب')),
                ('author', models.CharField(max_length=150, verbose_name='نویسنده')),
                ('publisher', models.CharField(max_length=100, verbose_name='انتشارات')),
                ('subject', models.IntegerField(choices=[(1, 'ادبیات'), (2, 'اسطوره\u200cای'), (3, 'اقتصاد'), (4, 'باستان\u200cشناسی'), (5, 'تاریخ'), (6, 'خاطره\u200cنویسی'), (7, 'رمان'), (8, 'داستان کوتاه'), (9, 'عرفان'), (10, 'دین'), (11, 'روان\u200cشناسی'), (14, 'جامعه\u200cنویسی'), (15, 'علوم\u200cانسانی'), (16, 'پزشکی'), (17, 'فلسفه'), (18, 'کودک و نوجوان'), (19, 'گزارش\u200cنویسی'), (20, 'مصاحبه'), (21, 'مقاله'), (22, 'موسیقی'), (23, 'هنر'), (24, 'سایر')], verbose_name='موضوع')),
                ('image', models.ImageField(blank=True, null=True, upload_to='entities/books', verbose_name='طرح روی جلد کتاب')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب',
            },
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('city', models.CharField(max_length=255, verbose_name='شهر')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('country', models.CharField(max_length=100, verbose_name='کشور')),
                ('province', models.CharField(max_length=100, verbose_name='استان/ایالت')),
            ],
            options={
                'verbose_name': 'سفر',
                'verbose_name_plural': 'سفر',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام فیلم')),
                ('director', models.CharField(max_length=100, verbose_name='نام کارگردان')),
                ('year', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=entities.models.current_year, verbose_name='سال تولید')),
                ('genre', models.IntegerField(choices=[(1, 'کمدی'), (2, 'درام'), (3, 'موزیکال'), (4, 'تریلر'), (5, 'اکشن'), (6, 'رمانتیک'), (7, 'ملودرام'), (8, 'معمایی'), (9, 'علمی-تخیلی'), (10, 'فانتزی'), (11, 'ترسناک'), (12, 'وسترن'), (13, 'نوآر'), (14, 'ماجراجویانه'), (15, 'سایر')], verbose_name='سبک')),
                ('image', models.ImageField(blank=True, null=True, upload_to='entities/films', verbose_name='پوستر فیلم')),
            ],
            options={
                'verbose_name': 'فیلم',
                'verbose_name_plural': 'فیلم',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام اثر')),
                ('singer', models.CharField(max_length=150, verbose_name='خواننده')),
                ('composer', models.CharField(max_length=150, verbose_name='آهنگساز')),
                ('songwriter', models.CharField(max_length=150, verbose_name='ترانه\u200cسرا')),
                ('image', models.ImageField(blank=True, null=True, upload_to='entities/songs', verbose_name='پوستر آلبوم یا ترانه')),
            ],
            options={
                'verbose_name': 'ترانه',
            },
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام اثر')),
                ('director', models.CharField(max_length=150, verbose_name='کارگردان')),
                ('scriptwriter', models.CharField(max_length=150, verbose_name='نمایشنامه\u200cنویس')),
                ('genre', models.IntegerField(choices=[(1, 'کمدی'), (2, 'درام'), (3, 'موزیکال'), (4, 'تریلر'), (5, 'اکشن'), (6, 'رمانتیک'), (7, 'ملودرام'), (8, 'معمایی'), (9, 'علمی-تخیلی'), (10, 'فانتزی'), (11, 'ترسناک'), (12, 'وسترن'), (13, 'نوآر'), (14, 'ماجراجویانه'), (15, 'سایر')], verbose_name='ژانر')),
                ('image', models.ImageField(blank=True, null=True, upload_to='entities/theater', verbose_name='پوستر تئاتر')),
            ],
            options={
                'verbose_name': 'تئاتر',
                'verbose_name_plural': 'تئاتر',
            },
        ),
        migrations.CreateModel(
            name='JourneyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100, verbose_name='نام عکس')),
                ('image', models.ImageField(upload_to=entities.models.JourneyImages.upload_to_gallery)),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.journey')),
            ],
        ),
    ]
