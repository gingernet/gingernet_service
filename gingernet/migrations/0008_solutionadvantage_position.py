# Generated by Django 2.2.7 on 2021-01-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gingernet', '0007_solutionadvantage_sequence'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutionadvantage',
            name='position',
            field=models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], default='NO', max_length=16, verbose_name='位置'),
        ),
    ]
