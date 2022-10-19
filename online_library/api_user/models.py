from django.db import models
from django.contrib.auth.models import User
from api_book.models import Book


class UserBook(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book')

    class Meta:
        abstract = True


class UserBookActivity(UserBook):

    page_number = models.SmallIntegerField(verbose_name='Current Page number')

    class Meta:
        verbose_name = "User's Book Activity"
        verbose_name_plural = "Users' Books Activities"

    # def __str__(self):
    #     return f'{self.user} {self.book} {self.page_number}'

    objects = models.Manager()


class UserLibraryActivity(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    books_read = models.ManyToManyField(
        Book,
        related_name='books+',
        related_query_name='books_read',
        # null=True,
        blank=True
    )
    books_in_process = models.ManyToManyField(
        Book,
        related_name='reading+',
        related_query_name='books_reading',
        # null=True,
        blank=True
    )

    class Meta:
        verbose_name = "User's Library Activity"
        verbose_name_plural = "Users' Library Activities"

    objects = models.Manager()


class UserHighlight(UserBook):

    page_number = models.SmallIntegerField(verbose_name='Page number')
    start_of_note = models.SmallIntegerField(verbose_name='Start position of the Note')
    end_of_note = models.SmallIntegerField(verbose_name='End position of the Note')
    note_text = models.TextField(verbose_name='Note Text')

    class Meta:
        verbose_name = "User's Highlight"
        verbose_name_plural = "Users' Highlights"

    objects = models.Manager()


class UserReview(UserBook):

    review_text = models.TextField(verbose_name='Review Text')
    rating = models.SmallIntegerField(verbose_name='Rating')

    class Meta:
        verbose_name = "User's Review"
        verbose_name_plural = "Users' Reviews"

    objects = models.Manager()
