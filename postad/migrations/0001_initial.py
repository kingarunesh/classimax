# Generated by Django 4.1.3 on 2022-11-14 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='PostAD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_id', models.UUIDField(default='5a0f9d8876f94bdbb0891e5f6aa3e147', editable=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image1', models.ImageField(upload_to='postad/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='postad/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='postad/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='postad/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='postad/')),
                ('price', models.IntegerField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False)),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('purchase_year', models.DateField()),
                ('sold', models.BooleanField(default=False)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('condition', models.CharField(choices=[('Almost Like New', 'Almost Like New'), ('Brand New', 'Brand New'), ('Gently Used', 'Gently Used'), ('Heavily Used', 'Heavily Used'), ('Unboxed', 'Unboxed')], max_length=100)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('NCR of Delhi', 'NCR of Delhi'), ('Puducherry', 'Puducherry')], max_length=100)),
                ('city', models.CharField(max_length=150)),
                ('seller_type', models.CharField(choices=[('Individual', 'Individual'), ('Dealer', 'Dealer')], max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postad', to='postad.category')),
                ('tag', models.ManyToManyField(related_name='postad', to='postad.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
