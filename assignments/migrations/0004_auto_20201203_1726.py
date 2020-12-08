# Generated by Django 3.1.3 on 2020-12-03 11:41

import assignments.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignments', '0003_auto_20201203_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadAssignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('upload_file', models.FileField(upload_to=assignments.models.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])),
                ('uploaded_date', models.DateField(auto_now_add=True, db_index=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upload_assignment', to='assignments.giveassignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upload_by_student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-uploaded_date',),
            },
        ),
        migrations.DeleteModel(
            name='UploadedAssignment',
        ),
    ]
