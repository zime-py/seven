# Generated by Django 3.1.1 on 2020-09-09 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_cool_embed_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cool',
            name='embed_code',
        ),
        migrations.RemoveField(
            model_name='cool',
            name='image',
        ),
    ]
