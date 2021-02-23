# Generated by Django 2.2.12 on 2021-01-30 21:13

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_prob', '0032_auto_20210130_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=2.946347568749974, null=True, verbose_name='Given this information, what is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]
