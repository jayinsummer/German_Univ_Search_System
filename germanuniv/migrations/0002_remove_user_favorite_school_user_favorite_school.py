# Generated by Django 4.2.13 on 2024-11-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('germanuniv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite_school',
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_school',
            field=models.ManyToManyField(related_name='favorited_by', to='germanuniv.school'),
        ),
    ]