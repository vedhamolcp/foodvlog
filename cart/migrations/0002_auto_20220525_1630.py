# Generated by Django 2.2 on 2022-05-25 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20220525_1544'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartlist',
            old_name='darte_added',
            new_name='date_added',
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quan', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cartlist')),
                ('prodt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Products')),
            ],
        ),
    ]