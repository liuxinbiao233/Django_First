# Generated by Django 2.0.5 on 2018-09-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
