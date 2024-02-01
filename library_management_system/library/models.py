from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
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
    HasBeenReturned = models.BooleanField(default=False)
    Fee = models.IntegerField(default=0)  
