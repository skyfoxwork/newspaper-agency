from django.urls import path

from agency.views import (
    IndexView,
    RedactorListView,
    RedactorDetailView,
    NewspapersCreateView,
    NewspapersUpdateView,
    NewspapersDeleteView,
    NewspapersListView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),
    path(
        "redactors/<int:pk>/detail/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"),
    path(
        "topics-create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
    path(
        "newspapers/",
        NewspapersListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "newspapers-create/",
        NewspapersCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspapers/<int:pk>/update/",
        NewspapersUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspapersDeleteView.as_view(),
        name="newspaper-delete"
    ),
]

app_name = "agency"
