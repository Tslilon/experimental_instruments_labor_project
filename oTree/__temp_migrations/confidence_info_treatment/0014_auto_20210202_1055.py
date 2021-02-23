# Generated by Django 2.2.12 on 2021-02-02 18:55

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('confidence_info_treatment', '0013_auto_20210202_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=74.30457377970966, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
    ]
