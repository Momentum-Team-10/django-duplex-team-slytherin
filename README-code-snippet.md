
# Code Snippet Manager


A Django application to manage snippets of code that a developer reuses often.


You need a good way to manage snippets of code you reuse often. You are going to build a web application that has these goals:

Logged in users can add code snippets.
Logged in users can search their own code snippets and get results.
Each user has a profile page that shows their public code snippets. Other users can copy a snippet with one click, adding it to their library of snippets.
How snippets work
A snippet has code (required), a language (required), a title (optional), and whatever other fields make sense. Some ideas to consider: a description or a list of tags.

If you copy a snippet by clicking the copy button (or whatever UI element is used for this purpose), there's a link back to the original snippet. The easiest way to do this is with a foreign key. One should be able to see how many times a snippet has been copied.

The reason why we copy snippets instead of "favorite" them is that they can change. The original snippet creator can edit their snippet; the copying user can edit their copy.

Requirements:

-Search function (should look for terms in title, description, tags? or langauge field)
-Copy button to copy snippet
-Show how many times a snippet is copied
-create users 
-Snippet creator can edit their snippet 
-Copying user can edit their copy

## Authors

-Keanya Phelps
-Jonathan Marsigli
-Trey Williams
-Jason Judkins

## Documentation

https://docs.djangoproject.com/en/3.2/

## Installation

$ pipenv install
$ pipenv shell
$ python manage.py migrate
$ python manage.py runserver
    


