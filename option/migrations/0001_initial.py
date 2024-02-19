# Generated by Django 5.0.2 on 2024-02-19 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('SINGLE', 'Single'), ('CHOICE', 'Choice'), ('BUTTON', 'Button'), ('TEXT', 'Text'), ('NUMBER', 'Number'), ('MULTIPLE_CHOICE', 'Multiple_choice')], max_length=16)),
                ('code', models.CharField(blank=True, max_length=31, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=255, null=True)),
                ('regex', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('is_required', models.BooleanField(default=False)),
                ('is_filter', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostOptionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OptionValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=256)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.option')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=256)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='option.option')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]