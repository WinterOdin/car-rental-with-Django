# Generated by Django 3.0.5 on 2020-07-28 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
