# Generated by Django 2.2.12 on 2021-01-24 06:09

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_pre', '0022_auto_20210123_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='self_rating',
            field=otree.db.models.IntegerField(default=4.191110215227326, null=True, verbose_name="How well do you think you'll do in the task? (0 = Very Badly, 10 = Very Well)"),
        ),
    ]
