# Generated by Django 4.1.2 on 2022-10-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('celeryApp', '0002_delete_generatefilelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenerateFileLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=200)),
                ('dataCount', models.IntegerField()),
            ],
        ),
    ]
