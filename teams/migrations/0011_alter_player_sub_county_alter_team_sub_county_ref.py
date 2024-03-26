# Generated by Django 4.1 on 2022-08-21 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0010_alter_coach_sub_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sub_county',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='county', chained_model_field='county', on_delete=django.db.models.deletion.CASCADE, to='teams.subcounty'),
        ),
        migrations.AlterField(
            model_name='team',
            name='sub_county',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='county', chained_model_field='county', on_delete=django.db.models.deletion.CASCADE, to='teams.subcounty'),
        ),
        migrations.CreateModel(
            name='Ref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='profile.png', upload_to='ref_images')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('id_No', models.IntegerField(unique=True)),
                ('birth_date', models.DateField()),
                ('ref_level', models.CharField(choices=[('Beginner', 'Beginner'), (' level 3', 'FiFA level 3'), (' level 2', 'FiFA level 2'), (' level 1', 'FiFA level 1')], default='Beginner', max_length=15)),
                ('position', models.CharField(choices=[('', ''), ('AR', 'Assistant Refereee'), ('CR', 'Centre Referee'), ('MC', 'Match Comm')], default='', max_length=15)),
                ('county', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.county')),
                ('sub_county', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='county', chained_model_field='county', on_delete=django.db.models.deletion.CASCADE, to='teams.subcounty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ref', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
