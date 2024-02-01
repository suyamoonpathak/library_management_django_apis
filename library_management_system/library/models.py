"""
models.py

This module defines the data models for the Library Management System.

User Model:
    - Represents a library user.
    - Fields:
        - UserID (AutoField): Unique identifier for the user.
        - Name (CharField): Name of the user.
        - Email (EmailField): Email address of the user (unique).
        - MembershipDate (DateField): Date when the user became a member of the library.

Book Model:
    - Represents a book in the library.
    - Fields:
        - BookID (AutoField): Unique identifier for the book.
        - Title (CharField): Title of the book.
        - ISBN (CharField): International Standard Book Number of the book (unique).
        - PublishedDate (DateField): Date when the book was published.
        - Genre (CharField): Genre of the book.

BookDetails Model:
    - Represents additional details about a book.
    - Fields:
        - DetailsID (AutoField): Unique identifier for the book details.
        - BookID (OneToOneField to Book): Reference to the corresponding book.
        - NumberOfPages (IntegerField): Number of pages in the book.
        - Publisher (CharField): Publisher of the book.
        - Language (CharField): Language of the book.

BorrowedBooks Model:
    - Represents a record of a user borrowing a book.
    - Fields:
        - UserID (ForeignKey to User): Reference to the borrowing user.
        - BookID (ForeignKey to Book): Reference to the borrowed book.
        - BorrowDate (DateField): Date when the book was borrowed.
        - ReturnDate (DateField): Date when the book is expected to be returned.

        - HasBeenReturned (BooleanField): Indicates whether the book has been returned (default: False).
        - Fee (IntegerField): Fee charged if the book is returned after the expected return date (default: 0).

Usage:
    - Integrate these models into your Django app for managing user and book-related data.
    - Use Django migrations to apply these models to your database.
    - Leverage the Django admin interface or custom views to interact with and manage the data.

Author: Suyamoon Pathak
Date: 01-02-2024
"""

from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, unique=True)
    MembershipDate = models.DateField()

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique = True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=100)

class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    BookID = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.IntegerField()
    Publisher = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)

class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField()
    #fields added on my own
    HasBeenReturned = models.BooleanField(default=False) #if the book has not be returned, this field is false, if it has been returned, it is true
    Fee = models.IntegerField(default=0) #If the day the user returned the book is past the returnDate he set while borrowing, user will be charge 10 rupees per day for the due period
