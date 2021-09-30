from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from .models import Profile
from .forms import Profile_Creation_Form
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

class Profile_Create_View(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = Profile_Creation_Form
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class Profile_Update_View(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = Profile_Creation_Form
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
