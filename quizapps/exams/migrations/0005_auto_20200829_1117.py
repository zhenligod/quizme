# Generated by Django 3.1 on 2020-08-29 10:17

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_story_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='story',
            name='content',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='story',
            name='instruction',
            field=martor.models.MartorField(),
        ),
    ]
