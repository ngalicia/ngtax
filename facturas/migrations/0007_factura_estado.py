# Generated by Django 2.2.3 on 2021-02-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0006_auto_20210221_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='estado',
            field=models.IntegerField(default=1),
        ),
    ]
