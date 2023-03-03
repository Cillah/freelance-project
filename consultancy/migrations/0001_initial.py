# Generated by Django 4.1.5 on 2023-03-03 06:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('training_topic', models.CharField(max_length=200)),
                ('training_poster', models.ImageField(max_length=200, null=True, upload_to='training_poster')),
                ('speaker', models.CharField(max_length=200)),
                ('speaker_image', models.ImageField(max_length=200, null=True, upload_to='training_speaker')),
                ('date', models.DateField()),
                ('timings', models.CharField(max_length=200)),
                ('remarks', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
