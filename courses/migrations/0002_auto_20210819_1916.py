# Generated by Django 3.2.5 on 2021-08-19 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='Course_code',
            new_name='course_code',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='Course_duration',
            new_name='course_duration',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='Course_Instractor',
            new_name='course_instractor',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='Course_name',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='Course_shedule',
            new_name='course_shedule',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='Syllabus',
            new_name='syllabus',
        ),
    ]
