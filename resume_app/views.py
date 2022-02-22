from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
import os 
import mimetypes
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            name = form.cleaned_data.get('name')
            messages.success(request,f' Hello {name}, Your mail has been Sent')
            return redirect('index')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context)

def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'web.pdf'
    # Define the full file path
    filepath = BASE_DIR + '/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

