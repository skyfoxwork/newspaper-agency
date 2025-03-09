from django.urls import path, include

from accounts.views import (
    RedactorCrateView,
    RedactorUpdateView,
    RedactorDeleteView,
)

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(
        "redactors-create/",
        RedactorCrateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete"
    ),
]

app_name = "accounts"
