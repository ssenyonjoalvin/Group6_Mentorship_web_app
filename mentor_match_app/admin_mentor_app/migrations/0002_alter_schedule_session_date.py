# Generated by Django 5.0.7 on 2024-07-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_mentor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='session_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
