# Generated by Django 3.1.2 on 2020-10-13 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enninapp', '0005_auto_20201012_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
