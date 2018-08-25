# Generated by Django 2.0.7 on 2018-08-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('question', models.TextField()),
                ('admission_no', models.CharField(max_length=255)),
                ('interests', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_no', models.IntegerField()),
            ],
        ),
    ]
