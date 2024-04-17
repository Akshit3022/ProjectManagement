# Generated by Django 5.0.3 on 2024-04-16 09:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_projectallocation_taskdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectallocation',
            name='taskStartDate',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='ManageLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaveStartDate', models.DateField()),
                ('leaveEndDate', models.DateField()),
                ('leaveReason', models.CharField(max_length=500)),
                ('empName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaves_requested', to=settings.AUTH_USER_MODEL)),
                ('notifyTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaves_notified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]