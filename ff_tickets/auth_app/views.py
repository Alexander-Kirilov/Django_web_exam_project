from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login
from django.contrib.auth import mixins as auth_mixins

from ff_tickets.auth_app.forms import UserCreateForm, ProfileUpdateForm
from ff_tickets.auth_app.models import AppUser, Profile


class SignUpView(views.CreateView):
    template_name = 'auth/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'auth/login-page.html'
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'auth/profile-details-page.html'
    model = AppUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


class UserEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'auth/profile-edit-page.html'
    context_object_name = 'user'
    queryset = Profile.objects.all()
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'auth/profile-delete-page.html'
    model = AppUser
    success_url = reverse_lazy('index')
