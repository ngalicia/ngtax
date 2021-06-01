# Generated by Django 2.2.3 on 2021-02-21 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_auto_20210219_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='periodo',
            field=models.IntegerField(default='202001'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factura',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.Proveedor'),
        ),
    ]