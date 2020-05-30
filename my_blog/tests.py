from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status

#
# class ApiArticleMothodTests(TestCase):
#     def test_article_with_id_no_exist(self):
#         id = 100000
#         response = self.client.get(reverse('api:article'))
#         response_code = response.status_code
#         self.assertEqual(response_code == status.HTTP_200_OK or response==status.HTTP_204_NO_CONTENT)