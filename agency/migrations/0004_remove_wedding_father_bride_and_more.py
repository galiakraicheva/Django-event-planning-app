# Generated by Django 5.1.1 on 2024-09-17 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_remove_client_name_client_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wedding',
            name='father_bride',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='father_groom',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='mother_bride',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='mother_groom',
        ),
    ]
