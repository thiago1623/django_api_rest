# Generated by Django 3.1.7 on 2021-04-08 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_register', '0002_auto_20210408_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
