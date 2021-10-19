from django.views.generic.list      import MultipleObjectMixin
from django.views.generic.edit      import DeleteView
from accountapp.forms               import Account_Update_Form
from django.shortcuts               import render, HttpResponseRedirect
from django.urls.base               import reverse_lazy
from django.urls                    import reverse
from django.views.generic           import CreateView, DetailView, UpdateView
from django.contrib.auth.models     import User
from django.contrib.auth.forms      import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator

from accountapp.decorators          import account_ownership_required
from .models                        import HelloWorld
from Articleapp.models              import Article

has_ownership=[login_required, account_ownership_required]

@login_required
def hello_world(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            temp = request.POST.get('hello_world_input')

            new_hello = HelloWorld()
            new_hello.text = temp
            new_hello.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))

        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html',context={'hello_world_list':hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class Account_Create_View(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class Account_Detail_View(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(Account_Detail_View, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class Account_Update_View(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class= Account_Update_Form
    template_name = 'accountapp/update.html'
    success_url = reverse_lazy('accountapp:hello_world')



@method_decorator(has_ownership, 'post')
@method_decorator(has_ownership, 'get')
class Account_Delete_View(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
