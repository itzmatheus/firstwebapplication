from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulário enviado com sucesso!')
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'diversos/index.html', {'form':form})
    