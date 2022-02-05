from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import View, DetailView, UpdateView, CreateView, DeleteView
from webapp.models import Choice, Poll
from webapp.forms import ChoiceForm


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/create_choice.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        form.save_m2m()
        return redirect('poll_view', pk=poll.pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={"pk": self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/delete.html'
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={"pk": self.object.poll.pk})




