# Generated by Django 3.1.7 on 2022-04-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20220429_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='athletes',
            name='age',
            field=models.IntegerField(default='00'),
            preserve_default=False,
        ),
    ]
