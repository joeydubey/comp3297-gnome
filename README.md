# COMP3297 Software Engineering- GNOME

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

I suggest downloading a DB sqlite viewew if you are interested in lookin at and manipulating the DB. 


## Setting up Django

### Environment Setup: Pipenv

`pip install pipenv` will install an isolated environment to maintain projects

### Repo Setup

cd into your directory

`pipenv install django` will install Django in your virtual environment

## Working on Code: Using Git

When you start working on code, you don't want to disrupt the current system. We will be using git. 
Each time you want to work on a feature or a task, you'll create a new branch. 
Start by pulling all the current code from master `git pull` and then `git checkout -b sprint-number/description` to 
create a new independant branch. You will now be on this new branch. Write all your code for this user story / individual
task on this branch, adding code `git add .` to add all the changed files or `git add file-names` to add specific files,
and making commits `git commit -m "descriptive commit message- what changes were made so we can track progress and rollback 
changes"` when necessary.

When you are done with making changes, push all of your commits `git push origin branch-name`. 


### Create Pull Requests
On the home page of our github reposotory after you've pushed your changes on your development branch. Click the green button "compare and pull request". Here you can describe what changes were made, make sure
all the tests pass, and assign specific developers to look over your code. Once another member approves your code, it will can
be merged into the master branch via the "squash and merge" button.

## Running Django

`python manage.py runserver` will launch the server where I have made some working pages!! http://127.0.0.1:8000/backtrack/projects will bring you to a page with a list of projects. You can use this to Debug and change your code based on the visual.


## Database changes
Feel free to make changes in Backtrack/Models.py, and then run to ensure your updates migrate throughout the project
```
python manage.py makemigrations backtrack
python manage.py migrate
```


## Writing tests
WRITE THEM!!! UNIT TESTS PLEASE!! I WIL BE TEST HOUND

### Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](ha put a link here) - The web framework used

## Authors

* **Hannah Grossman** - [Github](https://github.com/hannahg141)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


