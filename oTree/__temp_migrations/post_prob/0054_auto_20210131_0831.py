# Generated by Django 2.2.12 on 2021-01-31 16:31

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_prob', '0053_auto_20210131_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=41.79139566945415, null=True, verbose_name='Given this information, what is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]
