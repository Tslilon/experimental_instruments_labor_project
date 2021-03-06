# Generated by Django 2.2.12 on 2021-01-24 06:12

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prob_pre', '0007_auto_20210123_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=0.5322325019491126, null=True, verbose_name='Given the information, what is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]
