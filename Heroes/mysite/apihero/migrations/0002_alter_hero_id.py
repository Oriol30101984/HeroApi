# Generated by Django 4.0.4 on 2022-05-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apihero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
