# Generated by Django 4.2.7 on 2023-12-16 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_view_details_purchase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]