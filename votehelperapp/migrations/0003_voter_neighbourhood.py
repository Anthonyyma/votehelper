# Generated by Django 4.1.3 on 2022-12-18 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votehelperapp', '0002_alter_voter_decision_alter_voter_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='neighbourhood',
            field=models.TextField(default='none'),
        ),
    ]