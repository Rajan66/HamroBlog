# Generated by Django 4.2.3 on 2023-07-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fb_url',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='insta_url',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
