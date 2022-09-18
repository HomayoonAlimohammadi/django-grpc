from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate


User = get_user_model()


class UserModelTestCases(TestCase):
    def test_create_user_success(self):
        """Test creating user with .create and .save and is successful"""
        user = User.objects.create(username="username")
        user.set_password("password")
        user.save()
        user = User(username="username2")
        user.set_password("password2")
        user.save()
        self.assertEquals(User.objects.count(), 2)

        user_1 = User.objects.first()
        self.assertEquals(user_1.username, "username")  # type: ignore
        user_1 = authenticate(username="username", password="password")
        self.assertEquals(user_1.username, "username")  # type: ignore
        user_2 = User.objects.last()
        self.assertEquals(user_2.username, "username2")  # type: ignore
        user_2 = authenticate(username="username2", password="password2")
        self.assertEquals(user_2.username, "username2")  # type: ignore

    def test_deleting_user_is_successful(self):
        """Test user gets deletes successfuly and will not exist anymore."""
        User.objects.create(username="username", password="password")
        count = User.objects.count()
        self.assertEqual(count, 1)
        User.objects.filter(username="username").delete()
        count = User.objects.count()
        self.assertEqual(count, 0)
