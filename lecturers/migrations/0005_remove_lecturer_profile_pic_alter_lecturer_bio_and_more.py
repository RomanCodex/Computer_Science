# Generated by Django 4.1.3 on 2022-12-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturers', '0004_alter_lecturer_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='bio',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='facebook_username',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='github_username',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='hobbies',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
