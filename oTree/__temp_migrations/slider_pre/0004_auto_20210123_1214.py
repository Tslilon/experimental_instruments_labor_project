# Generated by Django 2.2.12 on 2021-01-23 20:14

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_pre', '0003_auto_20210123_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=otree.db.models.IntegerField(default=1.1011118041845014, null=True, verbose_name="How well do you think you'll do? (1 = Very Badly, 10 = Very Well)"),
        ),
    ]
