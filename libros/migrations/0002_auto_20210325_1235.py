# Generated by Django 2.2.3 on 2021-03-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librousado',
            name='fecha_uso',
        ),
        migrations.AddField(
            model_name='librousado',
            name='periodo',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
