from django.test import TestCase
from django.urls import reverse

from todo.models import Tag
from todo.models import Task


class TodoModelAndViewsTestCase(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")
        self.task = Task.objects.create(content="Finish Django project")
        self.task.tags.add(self.tag)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task), "Finish Django project")

    def test_tag_string_representation(self):
        self.assertEqual(str(self.tag), "Urgent")

    def test_task_list_view(self):
        response = self.client.get(reverse("todo:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Finish Django project")
