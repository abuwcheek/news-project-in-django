# Generated by Django 5.1.1 on 2024-09-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_newmodel_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmodel',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
