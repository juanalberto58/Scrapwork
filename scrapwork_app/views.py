from django.shortcuts import render
from django.http import HttpResponse
from .forms import workScrap

def nameScrap(request): 
    if request.method == 'POST':
        form = workScrap(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return render(request, 'works.html', {'name': name})
    else:
        form = workScrap()
    
    return render(request, 'nameScrap.html', {'form': form})

