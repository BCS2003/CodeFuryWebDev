# Generated by Django 4.1 on 2022-08-13 19:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='founders',
            field=models.ManyToManyField(related_name='co_founders', to=settings.AUTH_USER_MODEL),
        ),
    ]