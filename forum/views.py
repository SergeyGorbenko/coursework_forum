from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from forum.models import *

# Create your views here.
from forum.forms import Registration, CreatePost, CreateTag, ChangeProfile, CreateBook


def index(request):
    if request.method == 'GET':
        if request.GET.get('tag'):
            all_posts = Post.objects.filter(tags__name=request.GET.get('tag'))
        else:
            all_posts = Post.objects.all()
        form = CreatePost()
        context = {'posts': all_posts, 'form': form}
        return render(request, 'post/posts.html', context=context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        form = Registration()
        return render(request, 'registration/registration.html', {'form': form})
    elif request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            profile = UserProfile(user=User.objects.get(username=username))
            profile.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/registration.html', {'form': form})


def posts(request):
    if request.method == 'GET':
        if request.GET.get('tag'):
            all_posts = Post.objects.filter(tags__name=request.GET.get('tag'))
        else:
            all_posts = Post.objects.all()
        form = CreatePost()
        context = {'posts': all_posts, 'form': form}
        return render(request, 'post/posts.html', context=context)


def tags(request):
    all_tags = Tag.objects.all()
    form = CreateTag()
    context = {'tags': all_tags, 'form': form}
    return render(request, 'tag/tags.html', context=context)


def users(request):
    all_users = UserProfile.objects.all()
    context = {'users': all_users}
    return render(request, 'user/users.html', context=context)


def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            theme = request.POST.get('theme')
            context = request.POST.get('context')
            tags = str(request.POST.get('tags')).split(',')
            creator = UserProfile.objects.get(user=User.objects.get(username=request.user))
            post = Post(theme=theme, context=context, creator=creator)
            post.save()
            for tag in tags:
                try:
                    t = Tag.objects.get(name=tag)
                except Tag.DoesNotExist:
                    t = Tag.objects.create(name=tag, creator=creator)
                t.count += 1
                t.save()
                post.tags.add(t)
            post.save()
            creator.count_posts += 1
            creator.save()
            return redirect('/posts/')
        else:
            return render(request, 'post/posts.html', {'form': form})


def create_tag(request):
    if request.method == 'POST':
        form = CreateTag(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            context = form.cleaned_data.get('context')
            user = request.user
            creator = UserProfile.objects.get(user=User.objects.get(username=user))
            tag = Tag(name=name, context=context, creator=creator)
            tag.save()
            creator.count_tags += 1
            creator.save()
    return redirect('/tags/')


def create_comment(request, post_id):
    if request.method == 'POST':
        context = request.POST.get('context')
        creator = UserProfile.objects.get(user=User.objects.get(username=request.user))
        post = Post.objects.get(id=post_id)
        Comment.objects.create(creator=creator, context=context, post=post)
        return redirect(f"/posts/{post_id}/")


def my_profile(request):
    if request.method == 'POST':
        form = ChangeProfile(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            profile = UserProfile.objects.get(user__username=request.user)
            if str(request.user) != str(form.cleaned_data['username']):

                try:
                    if User.objects.get(username=form.cleaned_data['username']) or User.objects.get(
                            email=form.cleaned_data['email']):
                        context = {'form': form}
                        return render(request, 'user/profile.html', context=context)
                except User.DoesNotExist:
                    user.username = form.cleaned_data['username']
                    user.first_name = form.cleaned_data['first_name']
                    user.last_name = form.cleaned_data['last_name']
                    user.email = form.cleaned_data['email']
                    profile.about = form.cleaned_data['about']
                    profile.photo = form.cleaned_data['photo']
                    profile.user = user
                    profile.save()
            else:
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                profile.about = form.cleaned_data['about']
                profile.photo = form.cleaned_data['photo']
                profile.user = user
                profile.save()
            context = {'form': form, 'profile': profile}
            return render(request, 'user/profile.html', context=context)
        else:
            context = {'form': form}
            return render(request, 'user/profile.html', context=context)

    if request.method == 'GET':
        form = ChangeProfile()
        profile = UserProfile.objects.get(user=User.objects.get(username=request.user))
        context = {'form': form, 'profile': profile}
        return render(request, 'user/profile.html', context=context)


def profile(request, username):
    profile = UserProfile.objects.get(user=User.objects.get(username=username))
    context = {'profile': profile}
    if str(username) == str(request.user):
        return redirect('/profile/')
    return render(request, 'user/user_profile.html', context=context)


def post(request, post_id):
    current_post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=current_post)
    context = {'post': current_post, 'comments': comments}
    return render(request, 'post/post.html', context=context)


def books(request):
    all_books = Book.objects.all()
    form = CreateBook()
    context = {'books': all_books, 'form': form}
    return render(request, 'book/books.html', context=context)


def upload_book(request):
    if request.method == 'POST':
        form = CreateBook(request.POST, request.FILES)
        if form.is_valid():
            Book.objects.create(name=form.cleaned_data['name'],
                                authors=form.cleaned_data['authors'],
                                edition=form.cleaned_data['edition'],
                                description=form.cleaned_data['description'],
                                file=form.cleaned_data['file'],
                                creator=UserProfile.objects.get(user=User.objects.get(username=request.user)))
            return redirect('/books/')
        else:
            return render(request, 'book/books.html', {'form': form})


def book(request, book_id):
    one_book = Book.objects.get(id=book_id)
    context = {'book': one_book}
    return render(request, 'book/book.html', context=context)
