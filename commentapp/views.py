from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.utils.decorators import method_decorator

from Articleapp.models import Article

from .forms import Comment_Creation_Form
from .models import Comment
from .decorators import comment_ownership_required

class Comment_Create_View(CreateView):
    model = Comment
    form_class = Comment_Creation_Form
    template_name = 'commentapp/create.html'

    def form_valid(self, form):

        temp_comment = form.save(commit = False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})


@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class Comment_Delete_View(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})