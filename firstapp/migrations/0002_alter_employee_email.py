# Generated by Django 4.2.1 on 2023-05-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
