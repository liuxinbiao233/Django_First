# Generated by Django 2.1.1 on 2018-10-02 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180926_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='readnum',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog'),
        ),
    ]