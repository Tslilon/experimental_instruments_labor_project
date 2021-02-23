# Generated by Django 2.2.12 on 2021-02-02 05:54

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0129_auto_20210201_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=56.497433079297025, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=1.4226371626353929, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=4.08102652860901, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
