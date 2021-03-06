# Generated by Django 3.1.7 on 2021-04-11 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0008_auto_20210331_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(upload_to='Categorias'),
        ),
        migrations.AlterField(
            model_name='emprendedor',
            name='imagen',
            field=models.ImageField(upload_to='Emprendedores'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Descripción del Producto', max_length=60, null=True, verbose_name='descripción'),
        ),
    ]
