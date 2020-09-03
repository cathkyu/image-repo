from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Images
from .forms import ImageForm

# Create your views here.
def home_view(request):
    queryset = Images.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "home.html", context)

def create_view(request):
    
    # form = ImageForm(request.POST or None)
    form = ImageForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    
    context = {
        'form': form
    }

    return render(request, "create.html", context)