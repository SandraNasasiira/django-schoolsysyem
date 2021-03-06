# Generated by Django 3.2.5 on 2021-08-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20210819_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.PositiveIntegerField(blank='True', null='True'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bio',
            field=models.TextField(blank='True', null='True'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_hired',
            field=models.DateField(blank='True', null='True'),
        ),
    ]
