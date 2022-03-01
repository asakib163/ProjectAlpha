# Generated by Django 3.1.7 on 2021-03-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodsection', '0003_blood_donor_imag'),
    ]

    operations = [
        migrations.CreateModel(
            name='blood_bag_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_requester_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('blood_group', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_for_date', models.DateField()),
            ],
        ),
    ]