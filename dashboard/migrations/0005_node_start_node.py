# Generated by Django 2.0.7 on 2019-06-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20190607_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='start_node',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
