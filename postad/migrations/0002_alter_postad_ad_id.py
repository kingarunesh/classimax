# Generated by Django 4.1.3 on 2022-11-14 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postad',
            name='ad_id',
            field=models.UUIDField(default='5f09e29cbfaa4ef2bd4c8b12da53f39b', editable=False),
        ),
    ]
