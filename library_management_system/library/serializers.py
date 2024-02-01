from rest_framework import serializers
from .models import User, Book, BookDetails, BorrowedBooks
from datetime import timedelta

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'

class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = '__all__'
    
    def validate(self, data):
        if data['ReturnDate'] <= data['BorrowDate']:
            raise serializers.ValidationError("ReturnDate must be in the future compared to BorrowDate.")
        if data['ReturnDate'] - data['BorrowDate'] > timedelta(days=30):
            raise serializers.ValidationError("ReturnDate cannot be more than a month far from the BorrowDate.")
        return data


