# Generated by Django 3.1.7 on 2021-04-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210407_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, default='9999999999', max_length=10),
        ),
    ]