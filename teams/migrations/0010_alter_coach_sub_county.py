# Generated by Django 4.1 on 2022-08-21 10:18

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_rename_name_county_county_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='sub_county',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='county', chained_model_field='county', on_delete=django.db.models.deletion.CASCADE, to='teams.subcounty'),
        ),
    ]
