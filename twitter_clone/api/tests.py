from django.test import TestCase

from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            name='foo', screen_name= 'bar', email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.name, 'foo')
        self.assertEqual(user.screen_name, 'bar')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(screen_name='')
        with self.assertRaises(ValueError):
            User.objects.create_user(name='foo', screen_name= '', email='normal@user.com',  password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(name='foo', screen_name= 'bar', email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.name, 'foo')
        self.assertEqual(admin_user.screen_name, 'bar')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                name='foo', screen_name= 'bar', email='super@user.com', password='foo', is_superuser=False)