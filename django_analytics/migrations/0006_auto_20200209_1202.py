# Generated by Django 3.0.3 on 2020-02-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_analytics', '0005_auto_20200209_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalpagehit',
            name='page_url',
            field=models.CharField(help_text='The url that was accessed.', max_length=200),
        ),
        migrations.AlterField(
            model_name='visitorpagehit',
            name='page_url',
            field=models.CharField(help_text='The url that was accessed.', max_length=200),
        ),
    ]
