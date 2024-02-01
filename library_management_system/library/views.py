from django.shortcuts import render

from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer
from datetime import date

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailsViewSet(viewsets.ModelViewSet):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer

class BorrowedBooksViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['HasBeenReturned'] = False  # Set HasBeenReturned as False when borrowing a book
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
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

    @action(detail=False, url_path='all')
    def list_all(self, request):
        queryset = BorrowedBooks.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path='current')
    def list_current(self, request):
        queryset = BorrowedBooks.objects.filter(HasBeenReturned=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

