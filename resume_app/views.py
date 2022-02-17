from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

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