# Generated by Django 4.2 on 2023-06-07 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_rename_comemnts_comemnt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comemnt',
            new_name='Comment',
        ),
    ]