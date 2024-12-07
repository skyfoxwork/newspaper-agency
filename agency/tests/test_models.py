from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Newspaper, Topic


class ModelTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name="test_topic_name",
        )

        self.assertEqual(
            str(topic),
            topic.name
        )

    def test_newspaper_str(self) -> None:
        redactor = get_user_model().objects.create(
            username="test",
            password="test123",
        )

        topic = Topic.objects.create(
            name="test_topic_name",
        )

        newspaper = Newspaper.objects.create(
            title="test_title",
            context="test_context",
            published_date="2024-11-30",
            topic=topic,
        )

        newspaper.publishers.set([redactor])

        self.assertEqual(
            str(newspaper),
            newspaper.title
        )
