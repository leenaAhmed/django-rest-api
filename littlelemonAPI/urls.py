from django.urls import path 
from . import views

urlpatterns = [
    # path('books',views.books, name='books'),
    path('books',views.BookList.as_view()),
    path('books/<int:pk>',views.Book.as_view()),

    # path('books', views.BookView.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create'
    #     }
    # ), name='books'),
    # path('books/<int:pk>',views.BookView.as_view(
    #      {
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'patch': 'partial_update',
    #         'delete': 'destroy',
    #     }
    # ), name='book'),
]


# Routing with SimpleRouter class in DRF
# from rest_framework.routers import SimpleRouter
# router = SimpleRouter(trailing_slash=False)
# router.register('books', views.BookView, basename='books')
# urlpatterns = router.urls
