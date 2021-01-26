# Generated by Django 2.2.12 on 2021-01-26 06:22

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_prob', '0004_auto_20210125_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=24.804829221503066, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]