# Generated by Django 5.0.2 on 2024-02-19 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('option', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postoption',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.post'),
        ),
        migrations.AddField(
            model_name='postoptionvalue',
            name='post_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.postoption'),
        ),
    ]
