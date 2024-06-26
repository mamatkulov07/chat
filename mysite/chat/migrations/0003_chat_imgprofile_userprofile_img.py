# Generated by Django 5.0.6 on 2024-06-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat_video_message_last_activity_message_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='imgprofile',
            field=models.ImageField(blank=True, null=True, upload_to='chat_imgprofile/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='userprofile_img/'),
        ),
    ]
