from django.test import TestCase # uses unittests framework in-built with Python
from django.contrib.auth.models import User, Group
from django.db.models import Count

# for testing the API itself
from rest_framework.test import APITestCase
from rest_framework.views import status
from django.urls import reverse

##########################
# NOTE: All of these tests create a dummy db!! No values you add normally are compared here!!
##########################

# test the User model
class modelsTests(TestCase):
    def testUserModel(self):
        # we should begin with no users...
        self.assertEquals(
            User.objects.count(),
            0
        )
        # create a test group
        Group.objects.create(name="Test")
        # create some demo users, 2 exactly...
        user = User.objects.create_user(username="test user", email="test@unittest.com")
        # add the first user to a group, not the second
    
        user.groups.add(Group.objects.get(name="Test"))
        # create the second user without any groups
        User.objects.create(username="another user", email="anothertest@unittest.com")

        # test they were created and saved....
        self.assertEquals(
            User.objects.count(),
            2
        )

        # filter our users by their groups, one is a real group, the second shouldn't exist...
        # filtering like this is creating a FROM User SELECT User.* WHERE groups_name IS ...
        users_in_test = User.objects.filter(groups_name="Test")
        users_in_bogus = User.objects.filter(groups_name="bogus")

        # test the group we know to exist actually exists...
        self.assertEquals(
            users_in_test.count(),
            1
        )

        # test the bogus group doesnt exist...
        self.assertEquals(
            users_in_bogus.count(),
            0
        )

    def testGroupModel(self):
        # TODO: Write a simple Group endpoint test!!
        # This endpoint should return data from the Group model
        # test making a new group and some filtering...
        pass
