# Generated by Django 2.2.12 on 2021-01-26 06:05

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prob_pre', '0026_auto_20210125_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=52.76366980012854, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]
