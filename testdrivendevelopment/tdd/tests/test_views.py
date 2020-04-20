from django.test import TestCase # uses unittests framework in-built with Python
from django.contrib.auth.models import User, Group
from django.db.models import Count

# for testing the API itself
from rest_framework.test import APITestCase
from rest_framework.views import status
from django.urls import reverse

class PostUserAPIModelViewSet(APITestCase):
    def testPOSTUser(self):
        # Start with some setup
        # we should begin with no users...
        self.assertEquals(
            User.objects.count(),
            0
        )
        # get the users endpoint
        url = "http://127.0.0.1:8000/users"
        # data to be sent as POST
        data = {
            "username" : "POSTtestUserName",
            "email": "test@unittest.com",
            "groups": []
        }
        # create and send the POST
        response = self.client.post(url, data=data, format="json")

        # Now run some tests
        # test the response code for code 201
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        # and test that it saved the new user to the db
        self.assertEquals(User.objects.count(), 1)
        # compare data and db saved info
        user = User.objects.first()
        self.assertEquals(data["username"], user.username)
        self.assertEquals(data["email"], user.email)
        self.assertEquals(data["groups"], user.groups)

# class UserinGroupViewSet(TestCase):
#     def testGroupSearchEndpoint(self):
#         # shouldn't be any users yet...
#         self.assertEquals(
#             User.objects.count(),
#             0
#         )

#         # create some demo users for several groups exactly...
#         User.objects.create(username="test user", email="test@unittest.com", groups=["Test"])
#         User.objects.create(username="another user", email="anothertest@unittest.com")
