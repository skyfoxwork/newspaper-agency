from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from accounts.models import Redactor
from agency.models import Newspaper


@login_required
def index(request):
    newspapers = Newspaper.objects.all()
    context = {
        "newspapers": newspapers
    }

    return render(request, "agency/index.html", context=context)


class NewspapersCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("agency:index")


class NewspapersUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy(LoginRequiredMixin, "agency:index")


class NewspapersDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:index")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = "agency/redactor_detail.html"
