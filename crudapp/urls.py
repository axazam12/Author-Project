from . import views
from django.urls import path
from . import views

urlpatterns = [

    path('createbook/', views.CreateBook, name='CreateBook'),
    path('index/', views.index, name='index'),
    path('', views.ListBooks, name='listbooks'),
    path('search/',views.SearchBook,name='search'),
    path('publisher/', views.CreatePublisher, name='CreatePublisher'),
    path('pub/', views.publisher, name='publisher'),
    path('detail/<int:book_id>', views.DetailsBook, name='detail'),
    path('update/<int:book_id>', views.UpdateBook, name='update'),
    path('delete/<int:book_id>', views.DeleteBook, name='delete'),
]