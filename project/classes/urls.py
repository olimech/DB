from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('author', author, name='author'),
    path('update/<int:id>/', updateBook, name='update'),
    path('bookView', BookView.as_view(), name='bookviem'),
    path('bookView', BookCreateView.as_view(), name='create'),
    path('updateView/<int:id>/', BookCreateView.as_view(), name='update'),
]