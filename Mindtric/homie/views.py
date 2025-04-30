from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'Lander.html')

def inder(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about1.html')

def games_index(request):
    return render(request, 'gamesindex.html')

def shells(request):
    return render(request, 'click10shells.html')

def lock(request):
    return render(request, 'locksmithPuzzle.html')

def finder(request):
    return render(request, 'pathfindersquest.html')

def reset(request):
    return render(request, 'ritualreset.html')

def sym(request):
    return render(request, 'symmetrysketch.html')

def needle(request):
    return render(request, 'threadtheneedle.html')

def Team(request):
    return render(request, 'about2.html')

def Music(request):
    return render(request, 'Music.html')

def Self(request):
    return render(request, 'self_guide.html')

def Book(request):
    return render(request, 'book.html')