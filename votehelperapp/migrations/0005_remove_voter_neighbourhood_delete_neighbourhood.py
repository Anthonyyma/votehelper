# Generated by Django 4.1.3 on 2022-12-19 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votehelperapp', '0004_neighbourhood_alter_voter_neighbourhood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='neighbourhood',
        ),
        migrations.DeleteModel(
            name='Neighbourhood',
        ),
    ]
