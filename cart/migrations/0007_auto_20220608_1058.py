# Generated by Django 2.2 on 2022-06-08 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20220531_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='prodt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Products'),
        ),
    ]
