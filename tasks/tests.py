from django.test import TestCase
from django.urls import reverse
from rest_framework import status

data_returned = {
    'description': 'hello',
    'completed': False,
    'title': 'hello'
}


class TaskApiTests(TestCase):

    def test_task_list_empty(self):
        """Initialy task list should be empty"""
        response = self.client.get(reverse('tasks:task_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_task_create(self):
        """Creation of task should return status=status.HTTP_201_CREATED"""
        response = self.client.post(
            '/tasks/', {'title': 'hello', 'description': 'hello'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data_returned)

    def test_task_detail_dun_exist(self):
        """Retrieving a task that doesn't exist should return 404"""
        response = self.client.get(reverse('tasks:task_detail', args=(333,)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_task_detail_lifecycle(self):
        """Creation, retrieval, deletion should perform as expected."""
        response = self.client.post(
            '/tasks/', {'title': 'hello', 'description': 'hello'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data_returned)

        response = self.client.get(reverse('tasks:task_detail', args=(1,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data_returned)

        response = self.client.delete(reverse('tasks:task_detail', args=(1,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('tasks:task_detail', args=(1,)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
