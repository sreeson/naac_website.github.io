# Generated by Django 3.2.11 on 2023-03-11 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0013_rename_year_of_publication_details3_3_2_year_of_publications'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details3_1_1',
            options={'permissions': [('can_edit_311', 'Can edit 311')]},
        ),
    ]
