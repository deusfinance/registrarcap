# Generated by Django 2.2 on 2020-12-22 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0006_trade_hash'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trade',
            options={'ordering': ('timestamp', 'block')},
        ),
    ]