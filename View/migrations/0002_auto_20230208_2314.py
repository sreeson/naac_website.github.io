# Generated by Django 3.2.11 on 2023-02-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details3_1_1',
            name='Amount_Sanctioned',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details3_1_1',
            name='Duration_of_the_project',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='details3_1_1',
            name='Year_of_Award',
            field=models.IntegerField(default=0),
        ),
    ]