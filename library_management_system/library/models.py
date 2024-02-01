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
