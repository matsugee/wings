# Generated by Django 2.1.7 on 2019-02-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wings', '0003_action_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='comment',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
