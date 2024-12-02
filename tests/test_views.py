from django.contrib.auth import get_user_model
from django.test import TestCase, Client
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
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_redactor_list(self):
        topic = Topic.objects.create(
            name="test_name",
        )

        newspaper = Newspaper.objects.create(
            title="test_title",
            context="test_context",
            published_date="2024-11-30",
            topic=topic,
        )
        newspaper.publishers.set([self.user])

        newspaper = Newspaper.objects.create(
            title="test_title",
            context="test_context",
            published_date="2024-11-30",
            topic=topic,
        )
        newspaper.publishers.set([self.user])

        response = self.client.get(URL)
        self.assertEqual(response.status_code, 200)

        redactor = Redactor.objects.all()

        self.assertEqual(list(response.context["redactor_list"]), list(redactor))
        self.assertTemplateUsed(response, "agency/redactor_list.html")
