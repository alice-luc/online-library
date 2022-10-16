from django.db import models


class Book(models.Model):

    slug = models.SlugField(help_text="A short label to build url")
    title = models.CharField(max_length=511, verbose_name='Book Title')
    num_of_pages = models.SmallIntegerField(verbose_name="Number of Pages")
    year_pub = models.SmallIntegerField(verbose_name='Publication year')
    cover = models.ImageField(verbose_name='Book cover')
    pdf_file = models.FileField(verbose_name='File', upload_to='')
    author = models.ManyToManyField('Author', verbose_name='Author(s)')
    category = models.ManyToManyField('Category', verbose_name='Category(ies)')

    class Meta:
        permissions = [
            ('can_download_book', 'Can download books'),
        ]
        verbose_name = "Book"

    def __str__(self):
        return self.title


class Author(models.Model):

    name = models.CharField(max_length=30, verbose_name='Name')
    surname = models.CharField(max_length=50, verbose_name='Surname')
    biography = models.TextField(verbose_name='Biography')
    photo = models.ImageField(verbose_name='Author photo')

    class Meta:

        verbose_name = "Author"

    def __str__(self):
        return f'{self.name} {self.surname}'


class Category(models.Model):

    slug = models.SlugField(help_text="A short label to build url")
    title = models.CharField(max_length=50, verbose_name='Category name')

    class Meta:

        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
