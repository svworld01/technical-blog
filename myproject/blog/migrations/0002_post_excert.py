# Generated by Django 3.0.6 on 2020-05-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excert',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]