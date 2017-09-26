# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return_self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books")
    def __str__(self):
        return_self.title

class ReviewManager(models.Model):
    def validate_review(self, post_data):
        errors = []
        if len(post_data['title']) < 1 or len(post_data['reivew']) < 1:
            errors.append('fields are required')
        if not "author" in post_data and len(post_data['new_author']) < 3:
            errors.append('new author names must 3 or more charaters')

        if "author" in post_data and len(post_data['new_author']) > 0 and len(post_data['new_author']) < 3:
            errors.append('new author names must be 3 or more characters')
        if not int(post_data['rating']) > 0 or not int(post_data['rating']) <= 5:
            errors.append('invalid rating')
        return errors

    def create_review(self, clean_data, user_id):
        the_author = None
        if len(clean_data['new_author']) < 1:
            the_author = Author.objects.get(id=int(clean_data['author']))
        else:
            the_author = Author.objects.create(name=clean_data['new_author'])

        the_book = None
        if not Book.objects.filter(title=clean_data['title']):
            the_book = Book.objects.create(
                title=clean_data['title'], author=the_author
            )
        else:
            the_book = Book.objects.get(title=clean_data['title'])
        self_create(
            review = clean_data['review'],
            rating = clean_data['rating'],
            book = the_book,
            reviewer = User.objects.get(id=user_id)
        )

    def recent_and_not(self):
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])

class Review(models.Model):
    review = models.TextField()
    ratings = models.IntegerField()
    book = models.ForeignKey(Book, related_name="reviews")
    reviewer = models.ForeignKey(User, related_name="reviews_left")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ReviewManager()
    def __str__(self):
        return "Book: {}".format(self.book.title)
