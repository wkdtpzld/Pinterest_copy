from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView

from commentapp.forms import Comment_Creation_Form
from .models import Article
from .forms import ArticleCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import article_ownership_required
from django.views.generic.edit import FormMixin

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'get')
class Article_Create_View(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit = False)
        temp_article.writer = self.request.user
        temp_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

class Article_Detail_View(DetailView, FormMixin):
    model = Article
    form_class = Comment_Creation_Form
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'get')
class Article_Update_View(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})


class Article_Delete_View(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'

class Article_List_View(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 3