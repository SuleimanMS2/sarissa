# Generated by Django 4.0.4 on 2022-05-14 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuqaro', '0025_rename_jshirr_fuqaro_jshir'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='davlat',
            options={'ordering': ['name'], 'verbose_name': 'Davlat', 'verbose_name_plural': 'Davlatlar'},
        ),
    ]
