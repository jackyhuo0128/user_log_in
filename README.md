Login-Counter
=============

CS 169 warmup

How to deploy to Heroku:
1) Follow this link to push the master branch to Heroku repo 
http://tomatohater.com/2012/01/23/migrating-a-django-app-to-heroku/
Only push master branch

2) Make sure requirements.txt, setup.py (from django download), and Procfile is present in the root directory of the project

3) There might be unneccesary packages in the requirements.txt if it is not generated in virtual environmnet, this will cause remote rejected when pushing to Heroku repo

4) The Procfile should have web: python manage.py runserver '0.0.0.0:$PORT'
Heroku selects a port by random and bind it to $PORT when starting

5) In console, run heroku ps:web=1 to start the Django app

6) Use heroku ps:restart to restart

7) To view Heroku log, use heroku logs

8) To use the Makefile to test, in console cd to the directory of Makefile, and use make func_tests TEST_SERVER=(your app url)