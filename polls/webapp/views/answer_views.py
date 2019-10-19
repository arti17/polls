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


class StatisticsView(View):
    def get(self, request, *args, **kwargs):
        poll_id = kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_id)
        answers = Answer.objects.filter(poll=poll_id)
        count_answers = {}
        for answer in answers:
            if answer.choice in count_answers:
                count_answers[answer.choice] += 1
            else:
                count_answers[answer.choice] = 1

        return render(request, 'answer/statistics.html', {'poll': poll, 'answers': answers, 'count_answers': count_answers})
