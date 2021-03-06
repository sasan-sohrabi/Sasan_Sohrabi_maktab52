# Generated by Django 3.2.5 on 2021-07-22 13:53

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('coffeelanding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cashier',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('modify_timestamp', models.DateTimeField(auto_now=True)),
                ('delete_timestamp', models.DateTimeField(blank=True, null=True)),
                ('phone_number', models.IntegerField(max_length=20)),
                ('national_code', models.IntegerField(max_length=15)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
