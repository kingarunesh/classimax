# Generated by Django 4.1.3 on 2022-11-17 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interestad',
            old_name='order_date',
            new_name='taken',
        ),
    ]
