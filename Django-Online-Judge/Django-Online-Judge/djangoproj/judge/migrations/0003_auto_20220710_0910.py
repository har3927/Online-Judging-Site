# Generated by Django 3.0 on 2022-07-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_auto_20220709_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='statement',
            field=models.CharField(max_length=2500),
        ),
    ]
