from django.db import models
from django.shortcuts               import get_object_or_404, render
from django.urls.base               import reverse
from django.views.generic           import RedirectView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator

from projectapp.models  import Projectapp
from Articleapp.models  import Article
from .models            import Subscription


@method_decorator(login_required,'get')
class Subscription_View(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):

        project = get_object_or_404(Projectapp, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(Subscription_View, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class Subscription_List_View(ListView):
    models = Article
    template_name = "subscribeapp/list.html"
    context_object_name = 'article_list'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)

        return article_list