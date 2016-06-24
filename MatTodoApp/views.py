from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
import datetime

# Create your views here.
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'MatTodoApp/index_unauthenticated.html')
    else:
        return render(request, 'MatTodoApp/index_authenticated.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
        return render(request, "registration/register.html",{'form':form})




def hours_ahead(request, increment):
    try:
        inc = int(increment)
    except ValueError:
        return Http404

    return render(request, 'time.html', {'time':datetime.datetime.now()+datetime.timedelta(hours=inc)})