# Generated by Django 2.2.12 on 2021-02-06 17:19

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('confidence_info_treatment', '0019_auto_20210206_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=20.431046227830773, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
    ]
