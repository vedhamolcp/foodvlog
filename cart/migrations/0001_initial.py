# Generated by Django 2.2 on 2022-05-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=250)),
                ('darte_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
