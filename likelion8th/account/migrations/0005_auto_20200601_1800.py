# Generated by Django 3.0.6 on 2020-06-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_customusermodel_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='nickname',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='phone',
            field=models.IntegerField(blank=True, help_text='only number', null=True),
        ),
    ]
