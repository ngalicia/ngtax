# Generated by Django 2.2.3 on 2021-02-20 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
