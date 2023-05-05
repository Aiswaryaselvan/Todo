from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Mytask
from.forms import Todoform
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView

class Listview(ListView):
    model =Mytask
    template_name ='home.html'
    context_object_name = 'Task1'

class Detailview(DetailView):
    model =Mytask
    template_name = 'detail.html'
    context_object_name = 'Task2'

class Updateview(UpdateView):
    model =Mytask
    template_name = 'update.html'
    context_object_name = 'Task3'
    fields = ('taskname','priority','date')
    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class Deleteview(DeleteView):
    model =Mytask
    template_name = 'delete.html'
    context_object_name = 'Task4'
    success_url = reverse_lazy('listview')

# Create your views here.
def add(request):
    Task = Mytask.objects.all()
    if request.method=='POST':
        taskname1=request.POST.get('Taskname','')
        priority1=request.POST.get('Priority','')
        date1=request.POST.get('Date','')
        task=Mytask(taskname=taskname1,priority=priority1,date=date1)  #red il ulladh models.py ilthe variable name
        task.save()
    return render(request,'home.html',{'Task1':Task})

#
def delete(request,taskid):
    task2=Mytask.objects.get(id=taskid)
    if request.method=='POST':
        task2.delete()
        return redirect('/')
    return render(request,'delete.html')

def Update(request,id1):
    task3=Mytask.objects.get(id=id1)
    form=Todoform(request.POST or None,instance=task3)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'t3':task3, 'form1':form})
