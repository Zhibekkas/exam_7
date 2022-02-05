from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.views.generic import View
from webapp.models import Choice, Poll, Answer


class AnswerView(View):

    def get(self, request):
        answers = Answer.objects.all()
        context = {
            'answers': answers
        }
        return render(request, 'answer/index.html', context={'answer': answers})

    def post(self, request):
        answers = Answer.objects.all()
        answers.poll = request.POST.get('poll')
        answers.answer = request.POST.get('answer')
        return render(request, 'poll/index.html')
