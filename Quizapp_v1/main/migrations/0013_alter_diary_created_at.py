# Generated by Django 4.1.6 on 2024-07-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_diary_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
