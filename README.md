# CS463 Final Exam Django Tasks

## Completing these instructions will allow you to answer questions on the final.

### Install Django in virtual environment or use an existing virtual env with django 2.1+ installed. PYTHON 3 is required!

If necessary: ```pip3 install -r requirements.txt```

> The db for the django project ships prepared with a db and a running app. Start the development server to get the app running and make sure you can view the site in a browser. Then proceed with the following.

1. Modify the urls.py by adding a new pattern for the path "people/", using the NetView class, and the name set to "people"

2. Modify ```base.html``` so that the People menu item loads the page showing all the people in the network. Make sure the people page shows list of people. Clicking a person will show their friends.

3. Modify ```get_context_data()``` method in ```views.PersonalNetView()``` so that the friend list also indicates the oldest friend. Note: The template has already been constructed, you just need to provide the data to the context variable called ```nbr```.

