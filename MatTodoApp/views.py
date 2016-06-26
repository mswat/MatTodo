from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import redirect, get_object_or_404
import datetime
from django.contrib.auth.decorators import login_required
from MatTodoApp.models import ToDoItem, Category
from MatTodoApp.forms import ToDoItemForm, CategoryForm

# Create your views here.
def index(request, errors=[]):
    errors = {}
    if not request.user.is_authenticated():
        return render(request, 'MatTodoApp/index_unauthenticated.html')
    else:
        if request.session.__contains__("errors"):
            errors["errors"] =  request.session["errors"]
            request.session.__delitem__("errors")
        return render(request, 'MatTodoApp/index_authenticated.html', errors)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
        return render(request, "registration/register.html",{'form':form})

@login_required(login_url='/')
def addToDo(request):
    if request.method =="POST":
        form = ToDoItemForm(request.POST, user=request.user)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('index')
    else:
        form = ToDoItemForm(user=request.user)
    return render(request,'MatTodoApp/createToDo.html', {'form':form} )

@login_required(login_url='/')
def modifyToDo(request,key):
    item = get_object_or_404(ToDoItem, id=key)
    form = ToDoItemForm(request.POST or None, instance=item, user=request.user)
    form.category.queryset = request.user.category_set
    if form.is_valid():
        item = form.save()
        return redirect('index')
    return render(request,'MatTodoApp/createToDo.html', {'form':form})

@login_required(login_url='/')
def deleteToDo(request, key):
    error_messages = []
    try:
        item = ToDoItem.objects.get(id=key)
        item.delete()
    except ToDoItem.DoesNotExist:
        error_messages.append("Item Does not exist for %s" % key)
    if error_messages:
        request.session["errors"]= error_messages
    return redirect('index')


@login_required(login_url='/')
def addCat(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.ownedBy = request.user
            item.save()
            return redirect('index')
    else:
        form = CategoryForm()

    return render(request, 'MatToDoApp/addCategory.html', {'form':form})

