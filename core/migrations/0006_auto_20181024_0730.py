# Generated by Django 2.1.2 on 2018-10-24 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_produto_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago', models.BooleanField(default=False)),
                ('campista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Campista')),
            ],
        ),
        migrations.RemoveField(
            model_name='fechamento',
            name='campista',
        ),
        migrations.RemoveField(
            model_name='fechamento',
            name='produto',
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Fechamento',
        ),
        migrations.AddField(
            model_name='compra',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto'),
        ),
    ]
