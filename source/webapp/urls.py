from django.urls import path
from webapp.views.poll import (IndexPollView, PollView, EditView, CreationView, DeletePollView)
from webapp.views.choice import (ChoiceCreateView, ChoiceUpdateView, ChoiceDeleteView)

urlpatterns = [
    path('', IndexPollView.as_view(), name="poll_index"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('poll/<int:pk>/edit/', EditView.as_view(), name="poll_edit"),
    path('poll/add/', CreationView.as_view(), name="poll_add"),
    path('poll/<int:pk>/delete/', DeletePollView.as_view(), name="poll_delete"),
    path('poll/<int:pk>/choice/add/', ChoiceCreateView.as_view(), name='choice_add'),
    path('choice/<int:pk>/edit/', ChoiceUpdateView.as_view(), name='choice_edit'),
    path('choice/<int:pk>/delete/', ChoiceDeleteView.as_view(), name='choice_delete')




]
