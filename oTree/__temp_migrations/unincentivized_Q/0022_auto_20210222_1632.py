# Generated by Django 2.2.12 on 2021-02-23 00:32

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('unincentivized_Q', '0021_auto_20210222_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='location',
            field=otree.db.models.IntegerField(blank=True, choices=[[1, 'location1'], [2, 'location2'], [3, 'location3'], [4, 'location4']], null=True, verbose_name='Where do you live?'),
        ),
    ]
