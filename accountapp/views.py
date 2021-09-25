from django.shortcuts import render, HttpResponseRedirect
from django.urls.base import reverse_lazy
from .models import HelloWorld
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def hello_world(request):

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello = HelloWorld()
        new_hello.text = temp
        new_hello.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',context={'hello_world_list':hello_world_list})

class Account_Create_View(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'