# Generated by Django 2.2.12 on 2021-01-26 06:20

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_slider', '0002_auto_20210125_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='self_rating',
            field=otree.db.models.IntegerField(default=7.160067073674696, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
