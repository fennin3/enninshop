# Generated by Django 3.1.2 on 2020-10-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enninapp', '0009_auto_20201014_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.FileField(default='default.jpg', upload_to=''),
        ),
    ]
