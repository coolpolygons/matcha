from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Assignment
from django.contrib.auth.decorators import login_required
from . import forms


def assignment_list(request):
    assignments = Assignment.objects.all().order_by('date')
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})


def assignment_detail(request, slug):
    assignment = Assignment.objects.get(slug=slug)
    return render(request, 'assignments/assignment_detail.html', {'assignment': assignment})


@login_required(login_url="/accounts/login/")
def assignment_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to database
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('assignments:list')
    else:
        form = forms.CreateArticle()

    return render(request, 'assignments/assignment_create.html', {'form': form})
