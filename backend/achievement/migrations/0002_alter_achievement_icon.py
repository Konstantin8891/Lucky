# Generated by Django 5.2.3 on 2025-06-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='icon',
            field=models.ImageField(upload_to='static/achievements'),
        ),
    ]
