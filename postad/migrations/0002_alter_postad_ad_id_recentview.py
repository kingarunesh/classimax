# Generated by Django 4.1.3 on 2022-11-20 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postad',
            name='ad_id',
            field=models.UUIDField(default='b3f0b4e474ad46ac987dd31d49a7f8f3', editable=False),
        ),
        migrations.CreateModel(
            name='RecentView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postad.postad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
