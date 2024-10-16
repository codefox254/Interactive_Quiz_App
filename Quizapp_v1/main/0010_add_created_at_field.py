# migration file: 0010_add_created_at_field.py
import datetime
from django.db import migrations, models

def set_default_date(apps, schema_editor):
    Diary = apps.get_model('main', 'Diary')
    for diary in Diary.objects.all():
        diary.created_at = datetime.date.today()
        diary.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_previous_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
            preserve_default=False,
        ),
        migrations.RunPython(set_default_date),
    ]
