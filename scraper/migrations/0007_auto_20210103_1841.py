# Generated by Django 3.1.4 on 2021-01-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0006_auto_20210103_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='comment_sort',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
