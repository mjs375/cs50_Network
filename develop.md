# NETWORK
### Project Development Notes


--------------------------------------------------------------------------------
$ source env/bin/activate *activate VENV* $ which python *check: "env"*
  $ python3 manage.py makemigrations *if any changes to Models.py*
  $ python3 manage.py migrate *if any changes to Models.py*
$ python3 manage.py runserver *run the Django server, open in web browser*
--------------------------------------------------------------------------------




- [x] Download Distribution Code: https://cdn.cs50.net/web/2020/spring/projects/4/network.zip

- [ ] PROFILE PAGE:
  - Display how many followers and how many people they follow
  - Display all posts from that user, latest-oldest order
  - IF SIGNED IN: display a Follow/Unfollow button (except on user's own page)





--------------------------------------------------------------------------------



- **Git Branching:**
  - *create a FEATURE branch for every new function/feature in the project: MAIN should only and always contain working, stable code.*
    - ```$ git checkout -b feature```
  - *add to Tests.py for every new feature, building a suite of bug-tests.*
  - *Merge the <feature> in once debugged.*
    - ```$ git checkout main``` *switch back to main branch*
    - ```$ git merge feature``` *merge feature INTO main*

- **Virtual Environment:** **
  - **Create venv:** ```$ python3 -m venv env```
  - **Activate venv:** ```$ source env/bin/activate```
  - **Confirm you're in:** ```$ which python``` => ```.../env/bin/python```
  - **Leave VENV:** ```$ deactivate```

- **Requirements.txt**: *all the installations another user has to acquire in order to use the project.*
  - ```$ pip freeze > requirements.txt```: *run this after close of project to output all dependencies (and versions) into a requirements.txt.*

– **Tests.py**
  -**network.yml:**

- **Admin Superuser Account:** *manage the SQlite database from an admin page built-in to Django, rather than command-line prompts.*
  - ```$ python3 manage.py createsuperuser```
  - username: *admin*
  - password: *debug*
