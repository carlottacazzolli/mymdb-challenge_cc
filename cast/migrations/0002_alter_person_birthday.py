# Generated by Django 5.1.3 on 2024-12-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(),
        ),
    ]