from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import PollForm
from webapp.models import Poll


class PollView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = '-create_date'
    paginate_by = 5


class PollDetail(DetailView):
    template_name = 'poll/poll_detail.html'
    model = Poll
    context_object_name = 'poll'


class PollCreateView(CreateView):
    template_name = 'poll/create_poll.html'
    model = Poll
    form_class = PollForm

    def get_success_url(self):
        return reverse('index')


class PollUpdateView(UpdateView):
    model = Poll
    class_form = PollForm
    template_name = 'poll/update_poll.html'
    context_object_name = 'poll'
    success_url = '/'
    fields = ['question']


class PollDeleteView(DeleteView):
    model = Poll
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        poll = self.get_object()
        return render(request, 'poll/delete_poll.html', {'poll': poll})

    def get_object(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, pk=poll_pk)
