# Generated by Django 2.2.12 on 2021-02-06 17:26

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ravens', '0016_auto_20210206_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=68.8822763047297, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=5.419586150622273, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=1.465036378925656, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
