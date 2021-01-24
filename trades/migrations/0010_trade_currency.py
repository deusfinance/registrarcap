# Generated by Django 2.2 on 2021-01-11 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0009_remove_trade_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trades.Currency'),
            preserve_default=False,
        ),
    ]