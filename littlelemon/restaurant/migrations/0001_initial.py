# Generated by Django 4.2.6 on 2023-10-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('no_of_guests', models.IntegerField(max_length=6)),
                ('bookingdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invetory', models.IntegerField(max_length=5)),
            ],
        ),
    ]
