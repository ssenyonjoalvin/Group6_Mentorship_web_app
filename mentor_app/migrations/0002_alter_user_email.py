# Generated by Django 5.0.7 on 2024-07-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=191),
        ),
    ]
