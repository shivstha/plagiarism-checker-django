# Generated by Django 3.1.3 on 2020-11-11 16:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20201111_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1342c59c-1291-42f2-a6cc-c3e30e3e52f7'), editable=False, primary_key=True, serialize=False),
        ),
    ]