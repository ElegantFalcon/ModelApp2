# Generated by Django 4.1 on 2022-08-10 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0003_productdetails_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='model_name',
            field=models.CharField(default='testmodel', max_length=100),
            preserve_default=False,
        ),
    ]