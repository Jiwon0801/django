from django.shortcuts import render, redirect
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies,}
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie = Movie(
            title=title,
            title_en=title_en,
            audience=audience,
            open_date=open_date,
            genre=genre,
            watch_grade=watch_grade,
            score=score,
            poster_url=poster_url,
            description=description,
        )
        movie.save()
        return redirect('movies:index')
    else:
        return render(request, 'movies/create.html')


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {'movie': movie,}
    return render(request, 'movies/detail.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.title_en = request.POST.get('title_en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open_date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch_grade')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        context = {'movie': movie,}
        return render(request, 'movies/update.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)
