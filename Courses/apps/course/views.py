# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        Course.objects.create(
            name=request.POST['name'],
            desc=request.POST['desc']
        )
    return redirect('/')

def confirm(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'courses/confirm.html', context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')
