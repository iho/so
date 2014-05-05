from django.test import TestCase

# Create your tests here.


class TestBasic(TestCase):

    "Basics tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1
