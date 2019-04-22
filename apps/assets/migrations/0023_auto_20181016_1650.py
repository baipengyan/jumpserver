# Generated by Django 2.1.1 on 2018-10-16 08:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0022_auto_20181012_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commandfilterrule',
            options={'ordering': ('-priority', 'action')},
        ),
        migrations.AlterField(
            model_name='commandfilterrule',
            name='priority',
            field=models.IntegerField(default=50, help_text='1-100, the higher will be match first', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='priority',
            field=models.IntegerField(default=20, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Priority'),
        ),
    ]