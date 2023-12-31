# Generated by Django 4.2.3 on 2023-07-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('BS', 'bedsitter'), ('V', 'villa'), ('M', 'mansion'), ('B', 'Bungalow')], max_length=24)),
                ('description', models.TextField()),
                ('rental_price', models.IntegerField()),
                ('buying_price', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('image_1', models.ImageField(upload_to='houses')),
                ('image_2', models.ImageField(upload_to='houses')),
                ('image_3', models.ImageField(upload_to='houses')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
