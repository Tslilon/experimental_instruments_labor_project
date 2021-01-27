# Generated by Django 2.2.12 on 2021-01-25 23:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prob_pre', '0016_auto_20210125_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=0.4639799278881215, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]
