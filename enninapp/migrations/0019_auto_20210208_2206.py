# Generated by Django 3.0.7 on 2021-02-08 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enninapp', '0018_auto_20210208_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]