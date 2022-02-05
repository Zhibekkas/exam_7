from django.urls import path
from webapp.views.poll import (IndexPollView, PollView, EditView, CreationView, DeletePollView)

urlpatterns = [
    path('', IndexPollView.as_view(), name="poll_index"),
    path('poll/<int:pk>/', PollView.as_view(), name="poll_view"),
    path('poll/<int:pk>/edit/', EditView.as_view(), name="poll_edit"),
    path('poll/add/', CreationView.as_view(), name="poll_add"),
    path('poll/<int:pk>/delete/', DeletePollView.as_view(), name="poll_delete")





]
