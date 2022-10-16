# Generated by Django 4.1.2 on 2022-10-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('biography', models.TextField(verbose_name='Biography')),
                ('photo', models.ImageField(upload_to='', verbose_name='Author photo')),
            ],
            options={
                'verbose_name': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='A short label to build url')),
                ('title', models.CharField(max_length=50, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='A short label to build url')),
                ('title', models.CharField(max_length=511, verbose_name='Book Title')),
                ('num_of_pages', models.SmallIntegerField(verbose_name='Number of Pages')),
                ('year_pub', models.SmallIntegerField(verbose_name='Publication year')),
                ('cover', models.ImageField(upload_to='', verbose_name='Book cover')),
                ('pdf_file', models.FilePathField(verbose_name='File path')),
                ('author', models.ManyToManyField(to='api.author', verbose_name='Author(s)')),
                ('category', models.ManyToManyField(to='api.category', verbose_name='Category(ies)')),
            ],
            options={
                'verbose_name': 'Book',
                'permissions': [('can_download_book', 'Can download books')],
            },
        ),
    ]