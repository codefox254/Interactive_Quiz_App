# Generated by Django 4.1.6 on 2024-07-09 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_diary_diary_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='created_at',
        ),
    ]
