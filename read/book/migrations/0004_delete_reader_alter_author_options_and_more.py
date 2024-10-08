# Generated by Django 5.0.8 on 2024-08-10 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_reader_alter_author_age'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reader',
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_books', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Author Name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='authors_photos/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='books_photos/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Book Title'),
        ),
    ]
