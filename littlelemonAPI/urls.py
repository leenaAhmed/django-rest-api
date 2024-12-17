from django.urls import path 
from . import views

urlpatterns = [
    # path('books',views.books, name='books'),
    path('books',views.BookList.as_view()),
    path('books/<int:pk>',views.Book.as_view()),
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('book-items', views.menu_items),
    path('book-items/<int:menuId>', views.menu_item),
    path('category/<int:pk>', views.category_detail, name='category-detail'),



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
