# Generated by Django 4.1.3 on 2022-12-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturers', '0003_alter_lecturer_gender_alter_lecturer_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='post',
            field=models.CharField(choices=[('Graduate Assistant', 'Graduate Assistant'), ('Assistant Lecturer', 'Assistant Lecturer'), ('Lecturer Grade II', 'Lecturer Grade II'), ('Lecturer Grade I', 'Lecturer Grade I'), ('Senior Lecturer', 'Senior Lecturer'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor')], max_length=255),
        ),
    ]