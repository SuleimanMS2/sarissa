# Generated by Django 4.0.4 on 2022-05-09 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuqaro', '0022_alter_usmir_familiya_alter_usmir_ism_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usmir',
            name='guvohnoma_raqam',
            field=models.BigIntegerField(verbose_name='guvohnoma seriyasi'),
        ),
    ]