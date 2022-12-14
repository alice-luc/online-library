# Generated by Django 4.1.2 on 2022-10-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_book', '0001_initial'),
        ('api_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlibraryactivity',
            name='books_in_process',
            field=models.ManyToManyField(null=True, related_name='reading+', related_query_name='books_reading', to='api_book.book'),
        ),
        migrations.AlterField(
            model_name='userlibraryactivity',
            name='books_read',
            field=models.ManyToManyField(null=True, related_name='books+', related_query_name='books_read', to='api_book.book'),
        ),
    ]
