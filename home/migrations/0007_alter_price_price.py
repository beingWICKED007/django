# Generated by Django 4.0.4 on 2022-05-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_otp_alter_price_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.CharField(choices=[('0 To 100', '0 To 100'), ('300 To 400', '300 To 400'), ('200 To 300', '200 To 300'), ('100 To 200', '100 To 200'), ('400 To 500', '400 To 500')], max_length=100),
        ),
    ]
