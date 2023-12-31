# Generated by Django 4.2.7 on 2023-11-09 18:59

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EduBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='اسم')),
                ('enrollment_start_datetime', django_jalali.db.models.jDateTimeField(verbose_name='تاریخ شروع انتخاب واحد')),
                ('enrollment_end_datetime', django_jalali.db.models.jDateTimeField(verbose_name='تاریخ پایان انتخاب واحد')),
                ('class_start_datetime', django_jalali.db.models.jDateTimeField(verbose_name='تاریخ شروع کلاس\u200cها')),
                ('class_end_datetime', django_jalali.db.models.jDateTimeField(verbose_name='تاریخ پایان کلاس\u200cها')),
                ('modify_start_datetime', django_jalali.db.models.jDateTimeField(verbose_name='تاریخ شروع حذف واضافه')),
                ('modify_end_datetime', django_jalali.db.models.jDateTimeField(verbose_name='تاریخ پایان حذف و اضافه')),
                ('emergency_course_drop_end_datetime', django_jalali.db.models.jDateTimeField(verbose_name='زمان حذف اضطراری')),
                ('exam_start_date', django_jalali.db.models.jDateField(verbose_name=' تاریخ شروع امتحان\u200cها')),
                ('term_end_date', django_jalali.db.models.jDateField(verbose_name='پایان ترم')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_day', django_jalali.db.models.jDateField(verbose_name='روز کلاس')),
                ('class_time', django_jalali.db.models.jDateTimeField(verbose_name='زمان کلاس')),
                ('exam_datetime', django_jalali.db.models.jDateTimeField(verbose_name='تاریخ امتحان')),
                ('exam_place', models.CharField(max_length=128, verbose_name='مکان امتحان')),
                ('capacity', models.IntegerField(verbose_name='ظرفیت')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_terms', to='EduBase.course', verbose_name='درس')),
            ],
        ),
    ]
