# Generated by Django 3.2.5 on 2021-07-18 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coffeelanding.category')),
            ],
        ),
        migrations.CreateModel(
            name='Menu_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Import name of menu item', max_length=30, verbose_name='Name of menu item')),
                ('price', models.FloatField(help_text='Price of item', verbose_name='Price of item')),
                ('discount', models.FloatField(help_text='Discount of item', verbose_name='Discount of item')),
                ('date_serve', models.DateTimeField(help_text='Data of creation', verbose_name='Date')),
                ('cooking_time_estimate', models.TimeField(help_text='Time spend to prepare', verbose_name='Time')),
                ('available', models.BooleanField(default=False, help_text='Is item available', verbose_name='Available')),
                ('img', models.FileField(default=None, help_text='Address of image', null=True, upload_to='menu_items/', verbose_name='Address')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeelanding.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_serve', models.DateTimeField(help_text='When customer ordered ...?', verbose_name='Date of order')),
                ('status', models.BooleanField(help_text='Status of order, exp.: WAITING, REQ and ...', verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_position', models.IntegerField(help_text='Position of table in coffee shop', verbose_name='Position of table')),
                ('capacity', models.IntegerField(help_text='Number of people can use table', verbose_name='Capacity')),
            ],
        ),
        migrations.CreateModel(
            name='SubOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(help_text='Count of product in order?', verbose_name='Count')),
                ('menu_items', models.ForeignKey(help_text='Related to which menu item?', on_delete=django.db.models.deletion.CASCADE, to='coffeelanding.menu_items', verbose_name='Menu item id')),
                ('order_id', models.ForeignKey(help_text='Related to which order?', on_delete=django.db.models.deletion.CASCADE, to='coffeelanding.order', verbose_name='Order id')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('final_price_with_discount', models.FloatField()),
                ('time_stamps', models.DateTimeField()),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeelanding.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='table_order',
            field=models.ForeignKey(help_text='In which table ordered ...?', on_delete=django.db.models.deletion.CASCADE, to='coffeelanding.tables', verbose_name='Table ordered'),
        ),
    ]
