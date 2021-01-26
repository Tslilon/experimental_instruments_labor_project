# Generated by Django 2.2.12 on 2021-01-24 00:33

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prob_pre', '0003_auto_20210123_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=2.3084596410344305, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]