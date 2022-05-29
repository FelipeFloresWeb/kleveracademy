
from django.test import TestCase
from django.contrib.auth.models import User


class Test_User(TestCase):

    def setUp(self):
        User.objects.create(username='testuser', first_name='test',
                            last_name='user', email='novo@email.com', password='testpassword')

    def test_retorno_str_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.__str__(), 'testuser')

    def test_retorno_email_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.email, 'novo@email.com')

    def test_retorno_password_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.password, 'testpassword')

    def test_retorno_first_name_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.first_name, 'test')

    def test_retorno_last_name_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.last_name, 'user')

    def test_retorno_username_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.username, 'testuser')

    def test_retorno_is_active_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.is_active, True)

    def test_retorno_is_staff_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.is_staff, False)

    def test_retorno_is_superuser_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.is_superuser, False)

    def test_retorno_last_login_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.last_login, None)

    def test_retorno_date_joined_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.date_joined, None)

    def test_retorno_groups_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.groups, [])

    def test_retorno_user_permissions_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.user_permissions, [])

    def test_retorno_is_anonymous_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.is_anonymous, False)

    def test_retorno_is_authenticated_(self):
        user1 = User.objects.get(username='testuser')
        self.assertEqual(user1.is_authenticated, True)
