from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, BookDetailsViewSet, BorrowedBooksViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'bookdetails', BookDetailsViewSet)
router.register(r'borrowedbooks', BorrowedBooksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
