# Generated by Django 2.2 on 2019-04-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogposts',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
