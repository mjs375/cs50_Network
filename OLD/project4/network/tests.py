from django.test import Client, TestCase # TestCase: will create new DB for testing purposes only
from .models import User, Post


"""
Run tests manually:
    $ python3 manage.py test
Run ON PUSH:
    1. Create .yml file
    2. $ git add/commit/push
    3. Check Github.com
"""

# # # Create your tests here.


class LogInTest(TestCase): # TEST LOGIN PROCESS
    def setUp(self): # create a dummy user
        self.credentials = {
        'username': 'testuser',
        'password': 'dummypassword',
        }
        User.objects.create_user(**self.credentials)
    def test_login(self): # try to login dummy user
        # send login data:
        response = self.client.post('/login', self.credentials, follow=True)
        # should be logged in now:
        self.assertTrue(response.context['user'].is_authenticated)


"""
class NetworkTestCase(TestCase):
    # 
    def setUp(self): # create dummy data for tests
        # Create users
        chip = User.objects.create(username="Chip", email="chip@munk.com", password="chipper")
        # dale = User.objects.create(username)
        # Create tweets
        #
        pass

    #
    def test_post_squeak(self):
        #
        self.assertEqual()
        pass



    def test_two(self):
        pass
"""


"""
Django uses Python's UNITTEST, a class-based approach to testing.



"""
