# Generated by Django 2.1.2 on 2018-10-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181024_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='quantidade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
