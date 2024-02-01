"""
serializers.py

This module contains serializers for the models in the Library Management System.

UserSerializer:
    - Serializes User model instances.
    - Inherits from serializers.ModelSerializer.
    - Meta class specifies the model and fields to include in the serialization.

BookSerializer:
    - Serializes Book model instances.
    - Inherits from serializers.ModelSerializer.
    - Meta class specifies the model and fields to include in the serialization.

BookDetailsSerializer:
    - Serializes BookDetails model instances.
    - Inherits from serializers.ModelSerializer.
    - Meta class specifies the model and fields to include in the serialization.

BorrowedBooksSerializer:
    - Serializes BorrowedBooks model instances.
    - Inherits from serializers.ModelSerializer.
    - Meta class specifies the model and fields to include in the serialization.
    - Includes custom validation to ensure a valid timeframe between BorrowDate and ReturnDate.

Usage:
    - Integrate these serializers into your Django app for converting model instances to and from JSON.
    - Use these serializers in conjunction with Django REST Framework views to handle data serialization and deserialization.

Author: Suyamoon Pathak
Date: 01-02-2024
"""



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
        """
        Custom validation for the BorrowedBooksSerializer.
        
        Validates that the ReturnDate is in the future compared to BorrowDate
        and the timeframe between BorrowDate and ReturnDate is not more than a month.
        
        Raises:
            serializers.ValidationError: If validation fails.
            
        Returns:
            data: Validated data.
        """
        if data['ReturnDate'] <= data['BorrowDate']:
            raise serializers.ValidationError("ReturnDate must be in the future compared to BorrowDate.")
        if data['ReturnDate'] - data['BorrowDate'] > timedelta(days=30):
            raise serializers.ValidationError("ReturnDate cannot be more than a month far from the BorrowDate.")
        return data


