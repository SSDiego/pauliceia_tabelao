from django.shortcuts import render
from .forms import formClass
from .models import form_table

# Create your views here.
def home(request):
    return render(request, 'home.html')

def form(request):
    form = formClass()
    if request.method == 'POST':
        form = formClass(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'form.html', context)