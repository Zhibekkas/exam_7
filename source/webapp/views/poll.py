from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from webapp.models import Poll, Choice
from webapp.forms import PollForm


class IndexPollView(ListView):
    model = Poll
    context_object_name = "poll"
    template_name = "poll/index.html"
    paginate_by = 5
    paginate_orphans = 0
    ordering = ['-creation_date']


class PollView(DetailView):
    template_name = 'poll/view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = self.object.choices.all()
        context['choices'] = choices
        return context


class EditView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class CreationView(CreateView):
    model = Poll
    template_name = 'poll/create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class DeletePollView(DeleteView):
    template_name = 'poll/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('poll_index')
