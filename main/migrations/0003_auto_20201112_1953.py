# Generated by Django 3.1.2 on 2020-11-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201112_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='123-456-7890', max_length=100),
        ),
    ]
