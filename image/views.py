from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def home(request):
    img = None  # Initialize the variable with a default value
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
        img = Image.objects.all()
    return render(request, 'image/index.html', {'img':img,'form': form})
