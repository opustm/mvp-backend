# Generated by Django 3.1.2 on 2021-01-11 00:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210111_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cb9d9955-dc31-4f3c-907d-c86af51190f2'), editable=False, primary_key=True, serialize=False),
        ),
    ]
