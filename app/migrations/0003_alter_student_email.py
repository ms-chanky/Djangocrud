# Generated by Django 5.0.2 on 2024-02-29 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='guler@gmail.com', max_length=254),
        ),
    ]
