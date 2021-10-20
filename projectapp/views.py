from django.shortcuts               import render
from django.views.generic           import CreateView, ListView, DetailView
from django.urls                    import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator
from django.views.generic.list      import MultipleObjectMixin

from Articleapp. models     import Article
from subscribeapp.models    import Subscription
from .models                import Projectapp
from .forms                 import ProjectCreationForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'get')
class Create_Project_View(CreateView):
    model = Projectapp
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})


class Detail_Project_View(DetailView, MultipleObjectMixin):
    model = Projectapp
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,project=project)
        

        object_list = Article.objects.filter(project=self.get_object())
        return super(Detail_Project_View, self).get_context_data(object_list=object_list, subscription=subscription , **kwargs)


class Project_list(ListView):
    model = Projectapp
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20