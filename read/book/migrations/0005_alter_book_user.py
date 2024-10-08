# Generated by Django 5.0.8 on 2024-08-10 09:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_delete_reader_alter_author_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_books', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
