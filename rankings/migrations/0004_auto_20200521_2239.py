# Generated by Django 3.0.6 on 2020-05-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0003_auto_20200521_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='elo_recent',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamyear',
            name='district',
            field=models.CharField(default='a', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamyear',
            name='name',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamyear',
            name='region',
            field=models.CharField(default='a', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]