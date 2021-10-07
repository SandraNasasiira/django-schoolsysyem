# Generated by Django 3.2.5 on 2021-08-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=30)),
                ('Phone_number', models.CharField(max_length=14)),
                ('Age', models.PositiveIntegerField()),
                ('Gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Female', max_length=7)),
                ('Nationality', models.CharField(max_length=30)),
                ('county', models.CharField(max_length=20)),
                ('National_id', models.CharField(max_length=40)),
                ('Languages', models.CharField(max_length=29)),
                ('Bio', models.TextField()),
                ('Date_hired', models.DateField()),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]