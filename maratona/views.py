from django.shortcuts import render
from maratona.models import Maratona

def index(request):
    maratona = Maratona.objects.all()
    return render(request, 'maratona.html', {
        'maratona': maratona,
    })