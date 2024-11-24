# Generated by Django 4.2.16 on 2024-11-22 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_task_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='tasks-media/'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='profile-media/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
