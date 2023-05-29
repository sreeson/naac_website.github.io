# Generated by Django 3.2.11 on 2023-02-15 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0007_details3_4_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details3_5_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_the_MoU_Collaboration_linkage', models.CharField(max_length=200)),
                ('Name_of_the_collaborating_agency_institution_industry_corporate_house_with_whom_the_MoU_collaboration_linkage_is_made_with_contact_details', models.CharField(max_length=60)),
                ('Year_of_signing_MoU_collaboration_linkage', models.DateField(default=None)),
                ('radiobutton3_5_1', models.CharField(choices=[('1 year', '1 year'), ('2 year', '2 year'), ('3 year', '3 year'), ('4 year', '4 year'), ('5 year', '5 year')], default=None, max_length=50)),
                ('List_the_actual_activities_under_each_MOU_and_web_inks_year_wise', models.CharField(max_length=200)),
                ('Link_to_the_relevant_document', models.CharField(max_length=200)),
            ],
        ),
    ]