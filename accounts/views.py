from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import RedactorCreationForm
from accounts.models import Redactor


class RedactorCrateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("agency:redactor-list")


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")
