# Generated by Django 3.0.3 on 2020-03-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitinfo',
            name='recruit_length',
            field=models.PositiveIntegerField(default=0, verbose_name='要求工龄'),
        ),
        migrations.AlterField(
            model_name='recruitinfo',
            name='recruit_num',
            field=models.PositiveIntegerField(default=0, verbose_name='人数'),
        ),
        migrations.AlterField(
            model_name='workerinfo',
            name='work_length',
            field=models.PositiveIntegerField(default=0, verbose_name='工龄'),
        ),
    ]