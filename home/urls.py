from django.urls import path
from home.views import home_view, add_book, edit_book

app_name = "home"

urlpatterns = [
    path("book_list/", home_view, name="book_list"),
    path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
]