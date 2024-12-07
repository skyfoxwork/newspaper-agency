from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Newspaper
from accounts.models import Redactor

URL = reverse("agency:redactor-list")


class PublicLoginRequireTest(TestCase):
    def test_login_required(self):
        response = self.client.get(URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateLoginRequireTest(TestCase):
    def setUp(self) -> None:
        self.user_first = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user_first)

        self.user_second = get_user_model().objects.create_user(
            username="test_second",
            password="test456"
        )

    def test_retrieve_redactor_list(self):
        response = self.client.get(URL)
        self.assertEqual(response.status_code, 200)

        redactor = Redactor.objects.all()

        self.assertEqual(
            list(response.context["redactor_list"]), list(redactor)
        )
        self.assertTemplateUsed(
            response, "agency/redactor_list.html"
        )
