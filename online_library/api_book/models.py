from django.db import models
from django.urls import reverse


class Book(models.Model):

    slug = models.SlugField(help_text="A short label to build url")
    title = models.CharField(max_length=511, verbose_name='Book Title')
    num_of_pages = models.SmallIntegerField(verbose_name="Number of Pages")
    year_pub = models.SmallIntegerField(verbose_name='Publication year')
    cover = models.ImageField(verbose_name='Book cover', upload_to='covers')
    pdf_file = models.FileField(verbose_name='File', upload_to='books')
    author = models.ManyToManyField('Author', verbose_name='Author(s)')
    genre = models.ManyToManyField('Genre', verbose_name='Category(ies)')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     """Returns the url to access a particular book instance."""
    #     return reverse('book-detail', args=[self.slug])

    class Meta:
        permissions = [
            ('can_upload_book', 'Can upload books'),
        ]
        verbose_name = "Book"

    objects = models.Manager()

class Author(models.Model):

    name = models.CharField(max_length=30, verbose_name='Name')
    surname = models.CharField(max_length=50, verbose_name='Surname')
    biography = models.TextField(verbose_name='Biography')
    photo = models.ImageField(verbose_name='Author photo')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:

        verbose_name = "Author"

    objects = models.Manager()


class Genre(models.Model):

    slug = models.SlugField(help_text="A short label to build url")
    title = models.CharField(max_length=50, verbose_name='Category name')

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    objects = models.Manager()

