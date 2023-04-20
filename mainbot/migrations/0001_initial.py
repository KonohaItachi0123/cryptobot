# Generated by Django 4.2 on 2023-04-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threadlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=30)),
                ('secret_key', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('min_val', models.IntegerField(default=0)),
                ('max_val', models.IntegerField(default=10)),
                ('interval_time', models.IntegerField(default=10)),
                ('marketing_symbol', models.CharField(max_length=20)),
                ('crypto_remain', models.CharField(max_length=30)),
            ],
        ),
    ]
