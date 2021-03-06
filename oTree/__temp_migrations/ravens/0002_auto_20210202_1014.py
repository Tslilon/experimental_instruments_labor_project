# Generated by Django 2.2.12 on 2021-02-02 18:14

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ravens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=54.44417972544095, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
        migrations.AddField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=8.889399091063938, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AddField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=6.5757827204101, null=True, verbose_name='How well do you think you did in the task?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='answer',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], null=True, verbose_name='Please choose an item that best fits the pattern:'),
        ),
    ]
