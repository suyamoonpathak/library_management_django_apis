"""
urls.py

This module contains URL configurations for the Library Management System app.

- DefaultRouter is used to automatically generate URL patterns for the viewsets.
- URLs include endpoints for managing users, books, book details, and borrowed books.
- Additional URLs are provided for user authentication: login and signup.

Usage:
    - Include these URLs in your Django app's main URL configuration.

Author: Suyamoon Pathak
Date: 01-02-2024
"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, BookDetailsViewSet, BorrowedBooksViewSet
from .auth_views import LoginView, SignupView

# Creating a router to automatically generate URL patterns for viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'bookdetails', BookDetailsViewSet)
router.register(r'borrowedbooks', BorrowedBooksViewSet)

urlpatterns = [
    # Include the automatically generated URLs from the router
    path('', include(router.urls)),

    # Additional URLs for user authentication
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
