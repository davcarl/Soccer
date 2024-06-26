# Generated by Django 4.1 on 2022-08-14 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_county_player_id_birth_cert_no_subcounty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='county_name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='sub_county_name',
        ),
        migrations.AddField(
            model_name='team',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.county'),
        ),
        migrations.AddField(
            model_name='team',
            name='sub_county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.subcounty'),
        ),
        migrations.AlterField(
            model_name='player',
            name='id_birth_cert_no',
            field=models.IntegerField(unique=True),
        ),
    ]
