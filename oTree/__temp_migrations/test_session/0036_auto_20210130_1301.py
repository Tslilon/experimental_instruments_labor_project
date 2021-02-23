# Generated by Django 2.2.12 on 2021-01-30 21:01

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0035_auto_20210130_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=72.64882013880495, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=8.041400707150645, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=3.784874705747364, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
