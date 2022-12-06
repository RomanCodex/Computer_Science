# Generated by Django 4.1.3 on 2022-12-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='student',
            name='bio',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='student',
            name='facebook_username',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='github_username',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='hobbies',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='student',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
