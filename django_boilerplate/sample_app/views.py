# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError, Http404
from django.shortcuts import get_object_or_404, redirect, render

from forms import *
from models import *

def view_homepage(request):
    return render(request, 'homepage.html', {})


# HOWTO: Sample Views

"""
def view_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            
            return redirect('sample.html', sample=sample)
    else:
        form = PublisherForm()
    
    return render(request, 'sample.html', {'sample': sample})
"""