from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Newspaper


URL_INDEX = reverse("agency:index")
URL_NEWSPAPERS = reverse("agency:newspaper-list")
URL_TOPICS = reverse("agency:topic-list")


class PublicLoginRequireTest(TestCase):
    def test_login_required_index(self):
        response = self.client.get(URL_INDEX)
        self.assertNotEqual(response.status_code, 302)

    def test_login_not_required_index(self):
        response = self.client.get(URL_INDEX)
        self.assertEqual(response.status_code, 200)

    def test_login_required_newspaper_list(self):
        response = self.client.get(URL_NEWSPAPERS)
        self.assertNotEqual(response.status_code, 200)

    def test_login_not_required_newspaper_list(self):
        response = self.client.get(URL_NEWSPAPERS)
        self.assertEqual(response.status_code, 302)

    def test_login_required_topics_list(self):
        response = self.client.get(URL_TOPICS)
        self.assertNotEqual(response.status_code, 200)

    def test_login_not_required_topics_list(self):
        response = self.client.get(URL_TOPICS)
        self.assertEqual(response.status_code, 302)


class PrivateLoginRequireTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

    def test_index_view(self):
        response = self.client.get(URL_INDEX)
        self.assertTemplateUsed(
            response, "agency/index.html"
        )

    def test_retrieve_topic_list(self):
        Topic.objects.create(
            name="test_topic_first",
        )

        Topic.objects.create(
            name="test_topic_second",
        )

        response = self.client.get(URL_TOPICS)
        self.assertEqual(response.status_code, 200)

        topics = Topic.objects.all()

        self.assertEqual(
            list(response.context["topic_list"]), list(topics)
        )

        self.assertNotEqual(
            list(response.context["topic_list"]),
            ["topic_one", "topic_two", "topic_three"]
        )

        self.assertEqual(Topic.objects.count(), 2)

        self.assertNotEqual(Topic.objects.count(), 3)

        self.assertTemplateUsed(
            response, "agency/topic_list.html"
        )


    def test_retrieve_newspaper_list(self):
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

        response = self.client.get(URL_NEWSPAPERS)
        self.assertEqual(response.status_code, 200)

        newspapers = Newspaper.objects.all()

        self.assertEqual(
            list(response.context["newspapers"]), list(newspapers)
        )

        self.assertEqual(Newspaper.objects.count(), 2)

        self.assertNotEqual(Newspaper.objects.count(), 3)

        self.assertTemplateUsed(
            response, "agency/newspaper_list.html"
        )
