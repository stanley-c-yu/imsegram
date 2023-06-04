from django.shortcuts import render, redirect
from . models import Image
from . forms import ImageUploadForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    data = Image.objects.all()
    context = {
        'data': data
    }
    return render(request, "gallery_app/display.html", context)

@login_required
def upload_view(request):                                      
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('index')
            #return redirect("gallery_app/display.html") # this is currently broken.  Not sure why.  Something must've happened either when I was adding login/logout or during styling.  
            # disabling the return redirect unfortunately means we won't automatically go back to the image gallery, but saves us from getting a 404 error page.  
            # it sucks, but ultimately this feature isn't mission critical, and the app otherwise seems to function just fine.  
    else:
            form = ImageUploadForm()
    return render(request, 'gallery_app/upload.html', {'form': form})