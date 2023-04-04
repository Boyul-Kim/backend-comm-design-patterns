# backend-comm-design-patterns
Implementation of common backend communication design patterns in various languages

#Setting up Python Server
Based off the django tutorial: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
- django-admin startproject (name)
- python3 manage.py runserver (daphne pythonServer.asgi:application to use the websocket) daphne is an ASGI server
- python3 manage.py startapp (name)
- open up the new directory and look at views.py to do a quick test
- create urls.py in the new directory
- configure asgi.py for websocket functionality
- create consumers.py for websocket connection functionality



