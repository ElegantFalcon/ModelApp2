# Generated by Django 4.1 on 2022-08-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0002_productdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='price',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
