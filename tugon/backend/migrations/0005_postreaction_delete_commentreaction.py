# Generated by Django 4.2 on 2023-05-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_userprofile_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=9)),
                ('post_id', models.CharField(max_length=14)),
                ('agency_id', models.CharField(max_length=9)),
            ],
        ),
        migrations.DeleteModel(
            name='CommentReaction',
        ),
    ]
