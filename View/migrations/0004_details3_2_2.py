# Generated by Django 3.2.11 on 2023-02-09 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0003_alter_details3_1_1_year_of_award'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details3_2_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.DateField(default=0)),
                ('Name_of_the_workshop_seminar_conference', models.CharField(max_length=200)),
                ('Number_of_Participants', models.IntegerField(default=0)),
                ('Date_From', models.DateField(default=0)),
                ('Date_To', models.DateField(default=0)),
                ('Link_to_the_Activity_report_on_the_website', models.URLField(default=None)),
            ],
        ),
    ]