# Generated by Django 4.2 on 2023-05-14 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetFit', '0013_alter_useractivity_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friends',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='posts_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='UserActivity',
        ),
    ]