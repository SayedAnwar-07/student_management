# Generated by Django 5.1.5 on 2025-02-01 04:41

import students.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='https://blog.coursify.me/wp-content/uploads/2018/08/plan-your-online-course.jpg', null=True, upload_to=students.models.student_name_dict),
        ),
    ]
