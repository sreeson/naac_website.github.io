# Generated by Django 3.2.11 on 2023-02-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details3_1_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_the_research_project_endowment', models.CharField(max_length=200)),
                ('Name_of_the_Principal_Investigator_Co_investigator', models.CharField(max_length=200)),
                ('Department_of_Principal_Investigator', models.CharField(max_length=200)),
                ('Name_of_the_Funding_Agency', models.CharField(max_length=200)),
                ('Government_non_Government', models.CharField(choices=[('Government', 'Government'), ('Non-Government', 'Non-Government')], max_length=20)),
            ],
        ),
    ]
