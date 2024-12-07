from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test",
            password="test123",
        )

        self.assertEqual(
            str(redactor),
            redactor.username
        )

    def test_create_redactor_with_years_of_experience(self) -> None:
        username = "test"
        password = "test123"
        years_of_experience = 10

        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )

        self.assertEqual(redactor.username, username)
        self.assertEqual(redactor.years_of_experience, years_of_experience)
        self.assertTrue(redactor.check_password(password))
