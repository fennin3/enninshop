# Generated by Django 3.1.2 on 2021-02-06 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0003_auto_20191117_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=200)),
                ('items', models.ManyToManyField(to='carts.OrderItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
