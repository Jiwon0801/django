# Generated by Django 2.2.2 on 2019-06-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
