from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from agency.models import Topic, Newspaper
from accounts.models import Redactor

# URL = reverse("agency:redactor-list")


class PublicLoginRequireTest(TestCase):
    def test_login_required(self):
        URL = reverse("agency:redactor-list")
        response = self.client.get(URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateLoginRequireTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_newspaper_list(self):
        URL = reverse("agency:newspaper-list")

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

        newspapers = Newspaper.objects.all()

        self.assertEqual(
            list(response.context["newspapers"]), list(newspapers)
        )
        self.assertTemplateUsed(
            response, "agency/newspaper_list.html"
        )

    def test_retrieve_topic_list(self):
        URL = reverse("agency:topic-list")

        Topic.objects.create(
            name="test_name_first",
        )

        Topic.objects.create(
            name="test_name_second",
        )

        response = self.client.get(URL)
        self.assertEqual(response.status_code, 200)

        topics = Topic.objects.all()

        self.assertEqual(
            list(response.context["topic_list"]), list(topics)
        )
        self.assertTemplateUsed(
            response, "agency/topic_list.html"
        )
