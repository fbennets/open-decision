# Generated by Django 2.0.7 on 2019-04-02 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_node_slugify'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='slugify',
            new_name='slug',
        ),
    ]
