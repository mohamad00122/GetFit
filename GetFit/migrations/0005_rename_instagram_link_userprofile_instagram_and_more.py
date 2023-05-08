# Generated by Django 4.2 on 2023-05-08 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetFit', '0004_userprofile_instagram_link_userprofile_twitter_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='instagram_link',
            new_name='instagram',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='twitter_link',
            new_name='twitter',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='goals',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
