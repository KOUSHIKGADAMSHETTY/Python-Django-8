# Generated by Django 5.0.8 on 2024-08-10 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]
