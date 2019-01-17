Django REST API sample app
=====
Fast, flexible and robust solution to expose REST API resources backed by Django models.
Features:
-  self documenting
-  api version control
-  fully extends Django's ORM and User model
-  built-in authentication (JWT and other methods)
-  built-in serialization in various formats (JSON, XML, YAML, etcetera)
-  Built-in api debugging and testing console (similar to Postman)
-  Deployable as a pip package


Requirements
=====
-  Python 3.7
-  pip3
-  pipenv
-  Git
-  Node
-  Npm


Installation
=====

::

  $ pip3 install pipenv
  $ pipenv install
  $ pipenv shell
  (blog) $ python manage.py migrate
  (blog) $ python manage.py runserver




https://djangoforbeginners.com/initial-setup/

API Endpoints
=====
-  /api/v1/posts/
-  /api/v1/posts/{i}
-  /api/v1/users/
-  /api/v1/users/{i}

-  /admin/
-  /api/docs/
-  /api/docs/schema
-  /api/docs/swagger

-  /api/auth/login/
-  /api/auth/logout/
-  /api/auth/password/change/
-  /api/auth/password/reset/
-  /api/auth/password/reset/confirm/
-  /api/auth/registration/
-  /api/auth/user/
