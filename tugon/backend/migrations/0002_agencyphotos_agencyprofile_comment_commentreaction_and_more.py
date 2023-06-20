# Generated by Django 4.2 on 2023-05-19 09:45

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.CharField(max_length=9)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=backend.models.upload_to)),
                ('photo_id', models.CharField(max_length=14)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('comment_id', models.CharField(blank=True, default='', max_length=14, null=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='AgencyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.CharField(max_length=9)),
                ('agency_background_photo', models.ImageField(blank=True, null=True, upload_to=backend.models.upload_to)),
                ('agency_acronym', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=14)),
                ('user_id', models.CharField(max_length=9)),
                ('comment_id', models.CharField(max_length=19)),
                ('content', models.TextField()),
                ('numb_likes', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='CommentReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=9)),
                ('agency_id', models.CharField(max_length=9)),
                ('comment_id', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=14, unique=True)),
                ('user_id', models.CharField(max_length=9)),
                ('agency_id', models.CharField(max_length=9)),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to=backend.models.upload_to)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('numb_likes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.CharField(max_length=19)),
                ('user_id', models.CharField(max_length=9)),
                ('content', models.TextField()),
                ('num_react', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=9)),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to=backend.models.upload_to)),
            ],
        ),
    ]
