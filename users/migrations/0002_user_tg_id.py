# Generated by Django 4.2.6 on 2023-10-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.CharField(blank=True, null=True, unique=True, verbose_name='телеграм id'),
        ),
    ]