# Generated by Django 2.2.12 on 2021-01-23 18:44

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_auto_20210123_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='c_later',
            field=otree.db.models.IntegerField(default=7.780614116141607, null=True, verbose_name="How well do you think you'll do?"),
        ),
    ]
