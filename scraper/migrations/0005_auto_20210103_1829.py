# Generated by Django 3.1.4 on 2021-01-03 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_auto_20210103_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
