from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import View

from webapp.models import Poll, Answer, Choice


class AnswerView(View):
    def get(self, request, *args, **kwargs):
        poll = self.get_object()
        return render(request, 'answer/answers.html', {'poll': poll})

    def get_object(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)

    def post(self, request, *args, **kwargs):
        poll_id = kwargs.get('pk')
        choice_id = int(request.POST.get('answer'))

        pull = get_object_or_404(Poll, pk=poll_id)
        choice = get_object_or_404(Choice, pk=choice_id)
        answer = Answer()
        answer.poll = pull
        answer.choice = choice
        answer.save()
        return redirect('index')
