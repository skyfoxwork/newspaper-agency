from django.urls import path

from agency.views import (
    index,
    RedactorListView,
    RedactorDetailView,
    NewspapersCreateView,
    NewspapersUpdateView,
    NewspapersDeleteView,
    NewspapersListView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView, TopicDeleteView,
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
        "topic-list/",
        TopicListView.as_view(),
        name="topic-list"),
    path(
        "topic-crate/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
    path(
        "topic-update/<int:pk>/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topic-delete/<int:pk>/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "newspaper-list/",
        NewspapersListView.as_view(),
        name="newspaper-list"
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
