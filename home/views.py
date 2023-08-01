from django.shortcuts import render
from django.http import HttpResponse
from home.models import Task
# Create your views here.
def index(request):
    context = {'success': False , 'name':'Avinash'}
    if request.method =="POST":
        #handle the form
        title=request.POST['title']
        desc=request.POST['desc']
        print(title , desc)
        ins = Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context = {'success': True}

    #return HttpResponse("Home")
    return render(request,"index.html", context)
def task(request):
    #return HttpResponse("Home")
    allTasks = Task.objects.all()
    #print(allTasks)
    if request.method == 'POST':
        check=request.POST.getlist('checks[]')
        print(check)
        for i in check:
            b = Task.objects.get(taskTitle = i )
            b.delete()
    context = {'tasks': allTasks}
    return render(request, "task.html", context)






