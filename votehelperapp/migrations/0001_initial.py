# Generated by Django 4.1.3 on 2022-11-14 20:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('decision', models.CharField(max_length=20)),
                ('notes', models.TextField()),
            ],
        ),
    ]
