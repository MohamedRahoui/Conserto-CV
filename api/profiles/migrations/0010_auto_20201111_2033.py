# Generated by Django 3.0.4 on 2020-11-11 19:33

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20201108_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='focus_arias',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='functional_skills',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='technical_skills',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
