# Generated by Django 2.1.5 on 2020-09-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]