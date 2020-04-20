# Installation
1. Run a command window (Command prompt on windows or Terminal on Linux/MacOS) as admin/root.
2. cd to the project top-dir
3. attempt to run the setup script, `python3 setup.py`
4. If this throws any errors or returns early, let the presenter know so they can help finish the install!
..* If you are more familiar, setup is simply creating a virtualenv in the current dir then activating.
..* Simply pip3 install -r requirements in an activated environment to complete the setup!!
5. If the script worked for you, setup is complete!! We can now start!!

# Test Driven Development Workshop Demo
See below for the idea on what this is and how to run the demo!! Don't worry,
we'll run through this together in the workshop, :D.

Note: the site runs off the default sqlite3 shipped with Django.

## IDEA: 
To begin with as a demo, we have two simple User and Groups API routing setup.
- Each API endpoint exposes a viewset for a model, User or Groups
- calling the site root + model_in_lower_case returns a GET view (but I was nice and added POST too for viz)
..- a POST option is shown below to add new entries
- We will develop a new feature, looking up and returning all users in a given group!
- This will be done with the test driven development method

## Using the demo
1. cd to the project directory testdrivendevelopment
2. run python3 manage.py runserver
3. open the indicated link for the base URL
4. Login with the top right corner, admin w/ tdd123
5. Now the application will accept you!!

## Extending the demo
Now that we're familiar with the demo, let's extend it to include a new feature!!
We will add the capability to show a view with all users in a group, 
e.g.
    Group1
        user1
        user2
    Group2
        user4
    Group3
        user3
