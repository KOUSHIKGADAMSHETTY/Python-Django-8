from django.urls import path
from book import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('author/new/', views.newAuthor, name='Newauthor'),
    path('book/new/', views.newBook, name='Newbook'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('author/<int:author_id>/', views.author_details, name='author_details'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('book/delete/<int:book_id>/', views.deleteBook, name='delete_book'),
    path('author/delete/<int:author_id>/', views.deleteAuthor, name='delete_author'),
   # path('update/<int:book_id>/', views.update_view, name='update')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
