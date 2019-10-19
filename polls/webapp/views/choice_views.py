from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceCreateView(CreateView):
    template_name = 'choice/create_choice.html'
    form_class = ChoiceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        poll = self.get_object()
        context['poll'] = poll
        return context

    def form_valid(self, form):
        poll = self.get_object()
        poll.choices.create(**form.cleaned_data)
        return redirect('poll_detail', pk=poll.pk)

    def get_object(self, queryset=None):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        return poll


class ChoiceUpdateView(UpdateView):
    model = Choice
    class_form = ChoiceForm
    template_name = 'choice/update_choice.html'
    context_object_name = 'choice'
    success_url = '/'
    fields = ['text']


class ChoiceDeleteView(DeleteView):
    model = Choice
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        choice = self.get_object()
        return render(request, 'choice/delete_choice.html', {'choice': choice})

    def get_object(self):
        choice_pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, pk=choice_pk)
