# Generated by Django 5.0.3 on 2024-04-10 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_customuser_allocation_percentage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectallocation',
            old_name='user',
            new_name='emp_allocation',
        ),
    ]