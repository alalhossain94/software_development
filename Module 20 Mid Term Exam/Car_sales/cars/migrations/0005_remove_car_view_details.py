# Generated by Django 4.2.7 on 2023-12-16 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_delete_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='view_details',
        ),
    ]