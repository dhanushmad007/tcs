# Generated by Django 4.1 on 2024-11-17 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jloldata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jloldata',
            name='ol_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jloldata',
            name='dt_ct_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jloldata',
            name='joining',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jloldata',
            name='role',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jloldata',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]