# Generated by Django 5.0.6 on 2024-06-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AddField(
            model_name='message',
            name='last_activity',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='message',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]