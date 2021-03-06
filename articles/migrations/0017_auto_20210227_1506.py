# Generated by Django 2.2.13 on 2021-02-27 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20210227_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyComment',
            fields=[
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('articles.comment',),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='approved_by',
        ),
    ]