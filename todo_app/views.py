from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def home(request):
    return render(request, 'home.html')

def store_work(request):
    if request.method == 'POST':
        work = forms.TodoWorkForm(request.POST)
        if work.is_valid():
            work.save()
            print(work.cleaned_data)    
            return redirect('show_works')
    else:
        work = forms.TodoWorkForm()      
    return render(request, 'work_entre.html', {'form': work})

def show_works(request):
    work = models.TodoWorkModel.objects.all()
    print(work)
    return render(request, 'show_work.html', {'data': work})

def edit_work(request, id):
    work = models.TodoWorkModel.objects.get(pk = id)
    form = forms.TodoWorkForm(instance = work)
    if request.method == 'POST':
        info = forms.TodoWorkForm(request.POST, instance = work)
        if info.is_valid():
            info.save()  
            return redirect('show_works')
    else:
        return render(request, 'work_entre.html', {'form': form})
    
def delete_work(request, id):
    form = models.TodoWorkModel.objects.get(pk = id).delete()
    return redirect('show_works')

def complete_task(request, id):
    task = models.TodoWorkModel.objects.get(pk=id)
    task.status = True
    task.save()
    return redirect('completed_work') 

def completed_tasks(request):
    tasks = models.TodoWorkModel.objects.filter(status=True)
    return render(request, 'complete.html', {'data': tasks})