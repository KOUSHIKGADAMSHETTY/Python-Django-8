from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def Dashboard(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'user': request.user,
    }
    return render(request, 'dashboard.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('Dashboard')

    if request.method == "POST":
        n = request.POST.get('uname')  
        p = request.POST.get('passw')  
        user = authenticate(request, username=n, password=p)
        if user is not None:
            if user.is_authenticated:
                print(n, p, type(user))  
                auth_login(request, user)
                messages.success(request, "Welcome back!")
                return redirect('Dashboard')
            else:
                messages.error(request, "Account is inactive")
                return redirect('login')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='login')
def profile(request):
    print(request.user.username)
    return render(request, 'profile.html', {'user': request.user})


def register(request):
    if request.user.is_authenticated:
        return redirect('Dashboard')

    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        passw = request.POST.get('passw')
        cpass = request.POST.get('cpass')
        email = request.POST.get('email')
        uname = request.POST.get('uname')

        print(fname, lname, passw, cpass, email, uname)

        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')
        if len(passw) < 8:
            messages.error(request, "Password must be at least 8 characters")
            return redirect('register')
        if cpass != passw:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email, password=passw)
        messages.success(request, "Your account is ready, login now")
        return redirect('login')

    return render(request, 'register.html')

@login_required(login_url='login')
def newAuthor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        photo = request.FILES.get('photo')

        if name and age:
            author = Author(name=name, age=age, photo=photo)
            author.save()
            return redirect('Newbook')
    return render(request, 'author.html')

@login_required(login_url='login')
def newBook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        cost = request.POST.get('cost')
        rating = request.POST.get('rating')
        author_id = request.POST.get('author')
        photo = request.FILES.get('photo')

        if title and cost and rating and author_id:
            author = get_object_or_404(Author, pk=author_id)
            book = Book(title=title, cost=cost, rating=rating, author=author, photo=photo)
            book.save()
            return redirect('Dashboard')

    authors = Author.objects.all()
    return render(request, 'book.html', {'authors': authors})

@login_required(login_url='login')
def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_details.html', {'book': book})

@login_required(login_url='login')
def author_details(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'author_details.html', {'author': author})

@login_required(login_url='login')
def deleteBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.user.is_authenticated:
        book.delete()
        messages.success(request, "Book deleted successfully")
    else:
        messages.error(request, "You do not have permission to delete this book")

    return redirect('Dashboard')

@login_required(login_url='login')
def deleteAuthor(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.user.is_authenticated:
        author.delete()
        messages.success(request, "Author and their associated books deleted successfully")
    else:
        user_books = Book.objects.filter(author=author, author__user=request.user)
        if user_books.count() == Book.objects.filter(author=author).count():
            author.delete()
            messages.success(request, "Author and their books deleted successfully")
        else:
            messages.error(request, "You cannot delete this author as they are associated with other users' books")

    return redirect('Dashboard')

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out")
    return redirect('login')


'''
def update_view(request, book_id):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if not authenticated

    # Retrieve the book by ID
    book = get_object_or_404(Book, id=book_id)

    # Check if the user has permission to delete the book
    if request.method == 'POST':
        if 'delete' in request.POST:
            if request.user == book.user or request.user.is_superuser:
                book.delete()
                return redirect('dashboard')  # Redirect to profile or any other page
            else:
                return HttpResponse("Unauthorized", status=403)
        else:
            # Handle update logic if any form data is posted
            # For example:
            book.title = request.POST.get('title', book.title)
            book.cost = request.POST.get('cost', book.cost)
            book.rating = request.POST.get('rating', book.rating)
            book.save()
            return redirect('dashboard')  # Redirect to profile or any other page

    # For GET request, return the update page (you'll need to create this template)
    return render(request, 'update.html', {'book': book})
'''