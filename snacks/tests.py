from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnacksTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('snack_list')
        print(f"The url is {url}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")
        self.assertTemplateUsed(response, "snack_list.html")

        def test_thing_detail_view(self):
            response = self.client.get(reverse("thing_detail", args="1"))
            no_response = self.client.get("/100000/")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(no_response.status_code, 404)
            self.assertContains(response, "Reviewer: tester")
            self.assertTemplateUsed(response, "thing_detail.html")