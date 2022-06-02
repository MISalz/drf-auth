from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snacking


class SnackingTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_snacking = Snacking.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_snacking.save()

    # class 32
    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_snackings_model(self):
        snacking = Snacking.objects.get(id=1)
        actual_owner = str(snacking.owner)
        actual_name = str(snacking.name)
        actual_description = str(snacking.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_snacking_list(self):
        url = reverse("snacking_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snackings = response.data
        self.assertEqual(len(snackings), 1)
        self.assertEqual(snackings[0]["name"], "rake")

    def test_get_snacking_by_id(self):
        url = reverse("snacking_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacking = response.data
        self.assertEqual(snacking["name"], "rake")

    def test_create_snacking(self):
        url = reverse("snacking_list")
        data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        snackings = Snacking.objects.all()
        self.assertEqual(len(snackings), 2)
        self.assertEqual(Snacking.objects.get(id=2).name, "spoon")

    def test_update_snacking(self):
        url = reverse("snacking_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacking = Snacking.objects.get(id=1)
        self.assertEqual(snacking.name, data["name"])
        self.assertEqual(snacking.owner.id, data["owner"])
        self.assertEqual(snacking.description, data["description"])

    def test_delete_snacking(self):
        url = reverse("snacking_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        snackings = Snacking.objects.all()
        self.assertEqual(len(snackings), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("snacking_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)