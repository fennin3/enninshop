# Generated by Django 3.0.7 on 2021-02-08 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enninapp', '0016_auto_20210208_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
