# Generated by Django 2.1.2 on 2018-10-25 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20181025_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='nome',
            new_name='produto',
        ),
    ]
