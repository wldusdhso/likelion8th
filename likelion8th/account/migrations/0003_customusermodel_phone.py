# Generated by Django 3.0.6 on 2020-06-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200601_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]