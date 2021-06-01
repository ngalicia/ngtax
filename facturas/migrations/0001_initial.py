# Generated by Django 2.2.3 on 2021-02-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=15)),
                ('documento', models.IntegerField()),
                ('serie', models.CharField(max_length=15)),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('proveedor', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
    ]
