# Generated by Django 4.2.7 on 2023-12-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='First_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='musician',
            name='Last_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='musician',
            name='Phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
