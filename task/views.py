from django.shortcuts import render

# Create your views here.
from .models import Task
from .filters import filter_list

#Respobile to serve all  task objects to  frontend  temeplate.
def task_list(request):
    #param :  request 
    status = request.GET.get('status')  # Get the status from query params
    sort_by = request.GET.get('sort_by')  # Get the sort_by from query params
    print(sort_by)  # Debugging to see the sort_by value in the console/log

    tasks = filter_list(status, sort_by)

    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/task_list.html', context)

  