from django.urls import path

from agency.views import (
    index,
    RedactorListView,
    RedactorDetailView,
    NewspapersCreateView,
    NewspapersUpdateView,
    NewspapersDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("redactor-list/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactor-detail/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "newspaper-create/",
        NewspapersCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspaper-update/<int:pk>/",
        NewspapersUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspaper-delete/<int:pk>/",
        NewspapersDeleteView.as_view(),
        name="newspaper-delete"
    ),
]

app_name = "agency"
