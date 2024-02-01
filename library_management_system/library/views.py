"""
views.py

This module contains viewsets for handling CRUD operations on models in the Library Management System app.

UserViewSet:
    - Inherits from viewsets.ModelViewSet.
    - Handles CRUD operations for the User model.
    - Requires JWT authentication for access.
    - Requires the user to be authenticated.

BookViewSet:
    - Inherits from viewsets.ModelViewSet.
    - Handles CRUD operations for the Book model.
    - Requires JWT authentication for access.
    - Requires the user to be authenticated.

BookDetailsViewSet:
    - Inherits from viewsets.ModelViewSet.
    - Handles CRUD operations for the BookDetails model.
    - Requires JWT authentication for access.
    - Requires the user to be authenticated.

BorrowedBooksViewSet:
    - Inherits from viewsets.ModelViewSet.
    - Handles CRUD operations for the BorrowedBooks model.
    - Requires JWT authentication for access.
    - Requires the user to be authenticated.
    - Includes custom create and update methods for handling borrowing and returning books.
    - Provides additional actions for listing all borrowed books and currently borrowed books.

Usage:
    - Integrate these viewsets into your Django app's URL configuration.
    - Ensure that JWT authentication is set up in your Django project.
    - Use these viewsets with Django REST Framework views to handle CRUD operations on your models.

Author: Suyamoon Pathak
Date: 01-02-2024
"""


from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer
from datetime import date

class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet handles CRUD operations for the User model.
    Requires JWT authentication for access.
    Requires the user to be authenticated.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    BookViewSet handles CRUD operations for the Book model.
    Requires JWT authentication for access.
    Requires the user to be authenticated.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    

class BookDetailsViewSet(viewsets.ModelViewSet):
    """
    BookDetailsViewSet handles CRUD operations for the BookDetails model.
    Requires JWT authentication for access.
    Requires the user to be authenticated.
    """
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class BorrowedBooksViewSet(viewsets.ModelViewSet):
    """
    BorrowedBooksViewSet handles CRUD operations for the BorrowedBooks model.
    Requires JWT authentication for access.
    Requires the user to be authenticated.
    Includes custom create and update methods for handling borrowing and returning books.
    Provides additional actions for listing all borrowed books and currently borrowed books.
    """
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Custom method to handle the creation of a BorrowedBooks instance (borrowing a book).
        Sets HasBeenReturned to False when borrowing a book.
        """
        try:
            data = request.data.copy()
            data['HasBeenReturned'] = False  # Set HasBeenReturned as False when borrowing a book
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        """
        Custom method to handle the update of a BorrowedBooks instance (returning a book).
        Updates ReturnDate, Fee, and HasBeenReturned fields based on the return date provided.
        """
        try:
            instance = self.get_object()
            if instance.HasBeenReturned:
                raise ValidationError("This book has already been returned.")
            new_return_date = date.fromisoformat(request.data.get('ReturnDate'))
            if new_return_date < instance.BorrowDate:
                raise ValidationError("ReturnDate cannot be before BorrowDate.")
            if new_return_date > instance.ReturnDate:
                overdue_days = (new_return_date - instance.ReturnDate).days
                instance.Fee = overdue_days * 10
            instance.ReturnDate = new_return_date
            instance.HasBeenReturned = True
            instance.save()

            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except ValidationError as ve:
            return Response({'error': str(ve)}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, url_path='all')
    def list_all(self, request):
        """
        Custom action to list all borrowed books.
        """
        try:
            queryset = BorrowedBooks.objects.all()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @action(detail=False, url_path='current')
    def list_current(self, request):
        """
        Custom action to list currently borrowed books.
        """
        try:
            queryset = BorrowedBooks.objects.filter(HasBeenReturned=False)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


