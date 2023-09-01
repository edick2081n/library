from rest_framework.routers import DefaultRouter
from selection import views

router = DefaultRouter()
router.register('V1/authors', views.AuthorViewSet)
router.register('V1/books', views.BookViewSet)