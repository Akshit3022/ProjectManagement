# Generated by Django 5.0.3 on 2024-04-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='allocation_percentage',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
    ]