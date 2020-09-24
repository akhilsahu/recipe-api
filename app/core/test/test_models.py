import unittest

from django.contrib.auth import get_user_model


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_new_user_email_normalized(self):
        email = "test5665@dev.com"
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser("emaftil@email.com", 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)