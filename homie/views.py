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

def Shells(request):
    return render(request, 'click10shells.html')

def wordpuzzle(request):
    return render(request, 'wordpuzzle.html')

def Lock(request):
    return render(request, 'locksmithPuzzle.html')

def Finder(request):
    return render(request, 'pathfindersquest.html')

def Reset(request):
    return render(request, 'ritualreset.html')

def Sym(request):
    return render(request, 'symmetrysketch.html')

def needle(request):
    return render(request, 'threadtheneedle.html')

def wordbuilder(request):
    return render(request, 'wordbuilder.html')

def symphony(request):
    return render(request, 'symphony.html')

def voyager(request):
    return render(request, 'voyager.html')

def memmatch(request):
    return render(request, 'memmatch.html')

def zengarden(request):
    return render(request, 'zen.html')

def breath(request):
    return render(request, 'breath.html')

def soundscape(request):
    return render(request, 'soundscape.html')

def gentlepuzzle(request):
    return render(request, 'gentlepuzzle.html')

def jigsaw(request):
    return render(request, 'jigsaw.html')

def metaphor(request):
    return render(request, 'metaphor.html')

def constellation(request):
    return render(request, 'constellation.html')

def shadowwalk(request):
    return render(request, 'shadowwalk.html')

def Team(request):
    return render(request, 'about2.html')

def Music(request):
    return render(request, 'Music.html')

def Self(request):
    return render(request, 'self_guide.html')

def Book(request):
    return render(request, 'book.html')

def growthgarden(request):
    return render(request, 'growthgarden.html')

def thoughtfilter(request):
    return render(request, 'thoughtfilter.html')

def bubbleshooter(request):
    return render(request, 'bubbleshooter.html')

def hexaflow(request):
    return render(request, 'hexaflow.html')

def colortherapy(request):
    return render(request, 'colortherapy.html')

def pattern(request):
    return render(request, 'pattern.html')

def tetris(request):
    return render(request, 'tetris.html')
