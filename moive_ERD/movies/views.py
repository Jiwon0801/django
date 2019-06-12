from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Movie, Score, Genre


# Create your views here.
def index(request):
    #movies = Movie.objects.all()
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).order_by('?')
    context = {'movies': movies, }
    return render(request, 'movies/index.html', context)


def detail(request, movie_pk,):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movie_pk)
    scores = movie.score_set.order_by('-pk')
    genre = Genre.objects.get(pk=movie.genre_id
                              )
    context = {'movie': movie, 'scores': scores, 'genere':genre,}
    return render(request, 'movies/detail.html', context)


def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)


def scores_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST":
        content = request.POST.get('content')
        score = request.POST.get('score')
        comment = Score(movie=movie, content=content, score=score)
        comment.save()
        return redirect('movies:detail', movie.pk)
    else:
        return redirect('movies:detail', movie.pk)


def scores_delete(request, movie_pk, score_pk):
    comment = Score.objects.get(pk=score_pk)
    if request.method == "POST":
        comment.delete()
    return redirect('movies:detail', movie_pk)


def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.genre_id = request.POST.get('genre')
        movie.save()
        return redirect('movies:detail', movie_pk)
    else:
        genres = Genre.objects.all()
        context = {
            'movie': movie,
            'genres': genres,
        }
        return render(request, 'movies/update.html', context)
