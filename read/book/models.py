from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Author Name')
    age = models.IntegerField(verbose_name='Age')
    photo = models.ImageField(upload_to='authors_photos/', blank=True, null=True, verbose_name='Photo')

    def __str__(self):
        return self.name

   


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Book Title')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cost')
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Rating')
    photo = models.ImageField(upload_to='books_photos/', blank=True, null=True, verbose_name='Photo')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name='Author')
    def __str__(self):
        return self.title

 
