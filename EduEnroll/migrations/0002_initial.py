# Generated by Django 4.2.7 on 2023-11-09 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EduTerm', '0001_initial'),
        ('EduEnroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='course_term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student_courses', to='EduTerm.courseterm', verbose_name='درس ترم'),
        ),
    ]
