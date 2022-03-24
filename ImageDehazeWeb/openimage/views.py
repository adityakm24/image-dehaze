from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from .forms import ImageForm

# Create your views here.

def homeView(request):
    global img_obj
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance

            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})

def resultView(request):
    if request.method == 'POST' and 'run-script' in request.POST:
        import subprocess
        subprocess.call(f'python haze_removal.py {img_obj.uploadfile.name}')

        return render(request, 'results.html', {})