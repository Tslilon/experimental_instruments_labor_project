# Generated by Django 2.2.12 on 2021-02-02 00:58

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0114_auto_20210201_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=92.87479188198317, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=7.566167657082243, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=7.84612358193832, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
