from django.shortcuts import render
from.models import *
from django.http import *

def home(request):
    obj = student2.objects.all().order_by('name')
    return render(request, 'index.html', {'obj' : obj})


def student_detail(request):
    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studentform/')

    else:
        form = student_form()
        return render(request, 'student.html', {'form' : form})    