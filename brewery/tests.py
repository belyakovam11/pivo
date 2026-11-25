from django.test import TestCase
from django.urls import reverse

from .models import BuyerRegistration, EventRegistration, ProjectApplication


class BrewerySiteTests(TestCase):
    def test_homepage_renders_the_site(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Новости компании")
        self.assertContains(response, "Ближайшие события")
        self.assertContains(response, "Открытая варка")

    def test_private_and_wholesale_buyers_are_saved(self):
        private_response = self.client.post(
            reverse("register_buyer"),
            {"buyer_type": "private", "name": "Анна", "contact": "anna@example.com"},
        )
        wholesale_response = self.client.post(
            reverse("register_buyer"),
            {
                "buyer_type": "wholesale",
                "name": "Иван",
                "contact": "ivan@example.com",
                "company": "ООО Пиво",
            },
        )

        self.assertRedirects(private_response, reverse("home"))
        self.assertRedirects(wholesale_response, reverse("home"))
        self.assertEqual(BuyerRegistration.objects.count(), 2)
        self.assertEqual(
            BuyerRegistration.objects.get(name="Иван").buyer_type, "wholesale"
        )

    def test_wholesale_registration_requires_company(self):
        response = self.client.post(
            reverse("register_buyer"),
            {"buyer_type": "wholesale", "name": "Иван", "contact": "ivan@example.com"},
        )

        self.assertRedirects(response, reverse("home"))
        self.assertEqual(BuyerRegistration.objects.count(), 0)

    def test_event_and_project_forms_save_submissions(self):
        event_response = self.client.post(
            reverse("register_event"),
            {
                "event_title": "Дегустация",
                "name": "Анна",
                "contact": "anna@example.com",
                "guests": "2",
            },
        )
        project_response = self.client.post(
            reverse("submit_project"),
            {
                "name": "Команда",
                "contact": "team@example.com",
                "idea": "Пиво с цитрусом",
            },
        )

        self.assertRedirects(event_response, reverse("home"))
        self.assertRedirects(project_response, reverse("home"))
        self.assertEqual(EventRegistration.objects.count(), 1)
        self.assertEqual(ProjectApplication.objects.count(), 1)
