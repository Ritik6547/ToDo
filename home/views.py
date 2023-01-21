from django.shortcuts import render,HttpResponse
from home.models import Task

# Create your views here.
def index(request):
    context = {"success":False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']

        ins = Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context = {"success":True}
        

    return render(request,'index.html',context)

def task(request):
    allTask = Task.objects.all()
    # print(allTask)
    context = {"tasks" : allTask}
    return render(request,'task.html',context)
