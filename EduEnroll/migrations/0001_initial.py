# Generated by Django 4.2.7 on 2023-11-09 18:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'انتظار'), (2, 'تایید شده'), (3, 'رد شد')], default=1, verbose_name='وضعیت')),
                ('teacher_assistant_description', models.TextField(verbose_name='توضیحات استاد راهنما')),
                ('taken_term_number', models.IntegerField(verbose_name='توکن ترم')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'ثبت نام کرده'), (2, 'حذف شده'), (3, 'کامل شده')], verbose_name='وضعیت')),
                ('score', models.FloatField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='نمره')),
            ],
        ),
    ]
