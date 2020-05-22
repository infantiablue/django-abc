from django.test import TestCase
from courses.models import Subject, Course
from django.contrib.auth.models import User


class TestModels(TestCase):
    def test_subject_has_a_title(self):
        subj = Subject.objects.create(title="Programming")
        self.assertEqual(str(subj), "Programming")

    def test_course_has_students(self):
        instructor = User.objects.create(username="Bill")
        subj = Subject.objects.create(title="Programming")
        course = Course.objects.create(
            title="Django in Practice", owner=instructor, subject=subj)
        philip = User.objects.create(username="Philip")
        juliana = User.objects.create(username="Juliana")
        course.students.set([philip.pk, juliana.pk])
        self.assertEqual(course.students.count(), 2)
