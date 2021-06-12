# COMP3297 Software Engineering- GNOME 

# Limitations of final project
The final project lacks profiles for users where they can select between developer, scrum master, product owner, etc. and instead these types are managed through the user groups via the Django admin site. This configurability is odd and doesn't always work when we run Backtrack. We would hope in the next version to implement user profiles that are more managable by the actual users of Backtrack. 

The UI/UX is lacking what we would expect a final project to look like (however this was expected). 

Overall, the usability of adding/editing/selecting tasks/pbis isn't as seamless of a transition as we would have liked or that you would see in a professional project. Not using javascript made the coding simpler, but limited what we were really able to do. There are excess button pushes to complete a function from the user's viewpoint.

For the Burndown and Burnup charts, we weren't able to create this exactly as we wanted to because we don't currently track the work done per day or log an increase in actual effort hours per day to display this in a comprehensive chart. An update would be to log the day that a change in actual effort hours was made and use that to populate a chart and a graph.

When creating a new sprint, our goal was to select PBIs from the Product backlog to be added. We also wanted PBIs to to be added/removed from unstarted sprints. This unfortunatly didn't come to fruititon. We could implement a front end button to select PBIs however integrating this feature with the backend proved far more complicated than we expected. Becasue of this, transition a PBI into a new sprint, remove PBI from a sprint and, add a PBI to a sprint are features that didn't make it in release 1. (Some members also stopped replying to messages and didn't complete their share of the work and so we struggled to put the right amount of time into these features in order to successfully complete them).

# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

I suggest downloading a DB sqlite viewew if you are interested in lookin at and manipulating the DB. 


## Setting up Django

### Environment Setup: Pipenv

`pip install pipenv` will install an isolated environment to maintain projects

cd into your directory
`pipenv install django` will install Django in your virtual environment

activate your virtual environment with `pipenv shell`

## Working on Code: Using Git

When you start working on code, you don't want to disrupt the current system. We will be using git. 
Each time you want to work on a feature or a task, you'll create a new branch. 
Start by pulling all the current code from master `git pull` and then `git checkout -b sprint-number/description` to 
create a new independant branch. You will now be on this new branch. Write all your code for this user story / individual
task on this branch, adding code `git add .` to add all the changed files or `git add file-names` to add specific files,
and making commits `git commit -m "descriptive commit message- what changes were made so we can track progress and rollback 
changes"` when necessary.

When you are done with making changes, push all of your commits `git push origin branch-name`. 

create a new branch: `git checkout -b branchname`

change branches: `git checkout branchname`

deleting a branch: `git branch -D branchname`

what branch am I on? (suggest adding this to ur terminal- google it): `git branch`


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

## Built With

* [Django](ha put a link here) - The web framework used

## Authors

* **Hannah Grossman** - [Github](https://github.com/hannahg141)
* **Joey Pathak-Dubey** - [Github](https://github.com/joeydubey)
