# Generated by Django 2.2.3 on 2021-04-09 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0010_auto_20210408_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.IntegerField(choices=[('1', 'Activo'), ('2', 'Eliminado')], default=1),
        ),
    ]
