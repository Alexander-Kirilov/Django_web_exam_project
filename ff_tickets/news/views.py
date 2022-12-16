from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from ff_tickets.news.forms import NewsForm
from ff_tickets.news.models import News


class NewsListView(views.ListView):
    template_name = 'core/index.html'
    model = News

    def get_queryset(self, **kwargs):
        return News.objects.filter().order_by('-created_at')

# if you want to display the last 3 news
#     def get_queryset(self, **kwargs):
#         return News.objects.filter(is_private=False).order_by('-id')


class NewsAllListView(views.ListView):
    template_name = 'news/news_list_all.html'
    model = News
    ordering = ['-created_at']


class NewsCreateView(views.CreateView):
    template_name = 'news/news_create.html'
    form_class = NewsForm
    success_url = reverse_lazy('news_list_all')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class NewsDetailView(views.DetailView):
    template_name = 'news/news_detail.html'
    model = News


class NewsUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'news/news_edit.html'
    model = News
    fields = ('title', 'content', 'is_private', 'news_photos')
    success_url = reverse_lazy('news_list_all')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


class NewsDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'news/news_confirm_delete.html'
    model = News
    success_url = reverse_lazy('index')
