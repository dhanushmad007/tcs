# Generated by Django 4.1 on 2024-11-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JlolData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ct_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('joining', models.CharField(max_length=255)),
            ],
        ),
    ]