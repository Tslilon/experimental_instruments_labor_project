# Generated by Django 2.2.12 on 2021-02-02 00:55

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0112_auto_20210201_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=32.70208619288289, null=True, verbose_name='What is the probability that you outperformed 90% of the participants?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=7.677295585307464, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=7.997650687805487, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]