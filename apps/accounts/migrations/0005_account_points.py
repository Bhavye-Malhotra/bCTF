# Generated by Django 2.1.2 on 2018-11-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
