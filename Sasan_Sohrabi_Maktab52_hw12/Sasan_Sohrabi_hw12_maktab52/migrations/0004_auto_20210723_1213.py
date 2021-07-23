# Generated by Django 3.2.5 on 2021-07-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('coffeelanding', '0003_auto_20210722_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_items',
            name='cooking_time_estimate',
            field=models.TimeField(help_text='Time spend to prepare', null=True, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='menu_items',
            name='date_serve',
            field=models.DateTimeField(help_text='Data of creation', null=True, verbose_name='Date'),
        ),
        migrations.DeleteModel(
            name='Cashier',
        ),
    ]
