# Generated by Django 4.0.4 on 2022-05-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuqaro', '0003_rename_ona_passport_seriyasi_bazausmir_ona_pasport_seriya_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bazausmir',
            old_name='ona_pasport_seriya',
            new_name='ona_pasport_seriya1',
        ),
        migrations.RenameField(
            model_name='bazausmir',
            old_name='ota_pasport_raqami',
            new_name='ota_pasport_raqami1',
        ),
        migrations.RenameField(
            model_name='bazausmir',
            old_name='ota_pasport_seriya',
            new_name='ota_pasport_seriya1',
        ),
        migrations.RenameField(
            model_name='bazausmir',
            old_name='ota_shir',
            new_name='ota_shir1',
        ),
        migrations.RemoveField(
            model_name='bazausmir',
            name='ona_shir',
        ),
        migrations.RemoveField(
            model_name='bazausmir',
            name='ota_pasport_berilgan_vaqti',
        ),
        migrations.AddField(
            model_name='bazausmir',
            name='ona_shir1',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Ona JSHIR'),
        ),
    ]
