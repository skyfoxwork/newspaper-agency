from django.urls import path, include

from accounts.views import (
    RedactorCrateView,
    RedactorUpdateView,
    RedactorDeleteView,
)

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path(
        "redactor-create/",
        RedactorCrateView.as_view(),
        name="redactor-create"
    ),
    path(
        "redactor-update/<int:pk>/",
        RedactorUpdateView.as_view(),
        name="redactor-update"
    ),
    path(
        "redactor-delete/<int:pk>/",
        RedactorDeleteView.as_view(),
        name="redactor-delete"),
]

app_name = "accounts"
