# Generated by Django 3.0.7 on 2021-02-08 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enninapp', '0014_auto_20210208_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, help_text='Unique value for product page URl, created from name.', null=True, unique=True),
        ),
    ]
