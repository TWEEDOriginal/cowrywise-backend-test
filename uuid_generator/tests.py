import pytz
import os
from dotenv import load_dotenv
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import UUID_table

load_dotenv()
TIME_ZONE = os.getenv("TIME_ZONE")


class TestSetUp(APITestCase):
    def setUp(self):
        self.generate_url = reverse("api_route")
        return super().setUp()

    def tearDown(Self):
        return super().tearDown()


class TestUUIDgenerator(TestSetUp):
    def test_uuid_creation(self):
        response = self.client.post(self.generate_url, {}, format="json")
        uuid_table_count = (
            UUID_table.objects.all().count()
        )  # number of rows in the table
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), uuid_table_count)
        self.assertEqual(len(response.data), 1)

    # No API endpoint for deletion
    def test_uuid_cannot_be_deleted(self):
        response = self.client.delete(self.generate_url, {}, format="json")
        self.assertEqual(response.status_code, 405)

    # get all timestamp / uuid key value pairs
    def test_get_all_date_uuid_pairs(self):
        self.client.post(self.generate_url, {}, format="json")
        response = self.client.get(self.generate_url, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), dict)

    # check if the key value pair can be found in the table
    def test_compare_key_value(self):
        response = self.client.put(self.generate_url, {}, format="json")
        key = list(response.data.keys())[0]
        generated_uuid = UUID_table.objects.first()  # uuid table's first row

        date = generated_uuid.key.astimezone(pytz.timezone(TIME_ZONE)).strftime(
            "%Y-%m-%d %H:%M:%S.%f"
        )  # conversion to timezone becasue django saves date values in utc
        self.assertEqual(key, str(date))
        self.assertEqual(response.data[key], str(generated_uuid.value))
