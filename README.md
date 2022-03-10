# Wordle-Project

## Contents:
* The Project
* Project Planning
* Risk Assessment
* Ci Pipeline
* Testing
* The App
* What went wrong

## The Project:
The idea behind this project was to make a addition to the Wordle app (a game where you try guess a random 5 letter word in 6 guesses or less) that has taken off recently, by making a more detailed way of storing the guesses so the user is able to have a better understanding of the words they often use or do not use in their guesses.
The project was created using a a Automated CI pipeline. The apps i used to create the project are shown as follows:


##  Project Planning:
My first step to planning this project was to design a Entity Relationship Diagram(ERD). 
![ERD One](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/V1drawio.png)
initially in this design i came up with three tables the first being the user table which holds the user information needed for the login and to keep the data based on who is logged in. This has a zero to many relationship with Correct words which will store the correct words of the guesses as each word can have many guesses. Finally we have a 1 to many of correct words to guesses.

![ERD Two](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/final%20databasescheme.png)
This ERD  evolved during the process. The main change of this was adding in a LoggedUser table which one a one column table i used to store the ID of the user who was logged in so the information that was gathered throughout the process only affects the logged in User. I orginally designed it to use a global variable but as that was a unreliable decision i moved to a database to store it. If i was to continue to update it i would store the logged in user in a session. 

## Risk Assesment
During the design phase i mapped out a a risk assessment board of the risks that could potentially occur. 
![Risk Assessment](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/2022-03-10%2014_21_24-Window.png)
The most notable of these risks is risk 4 as currently in the stage the applicaiton is in there is very little security in place. The user passwords currently do not get encrypted in either the database or before they get sent off to the database. This would be a serious problem if this application were to go onto a live platform as attacks like a man in the middle attack would be able to get users passwords in their raw form allow them to access that users account. 

## CI Pipeline
The Ci pipeline I went with is as follows:
* Jira - Project tracking
* Git - Version control
* Jenkins - CI server
* GCP - Virtual machines hosting the app and database
* development enviroment - Python3


For project tracking i used Jira. I used this to keep track of the tasks. These tasks were split up into the seperate pages of the application which i focused on one by one and moved through the stages as i completed them.
![Jira board](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/Jiraboard2.png)

[Full Jira board](https://jack-middleton.atlassian.net/jira/software/projects/WOR/boards/6)

For version control i used Git which was hosted on github. This allowed me to use the inbuilt functionality it also has with visual studio to be able to push the completed code onto github. Along with using the Feature -> Dev -> Main funcitonality to be able to avoid pushing incomplete code to a live enviroment and fully test it before deployment. 

The development enviroment i used was Ubuntu on a virtual machine hosted by GCP. Using python3 as the main code base with imports of flask and sql academy to allow for links to SQL databases and HTML. 

I then used Jenkins as a CI server. Linking it to Git hub using web hooks allowed for jenkins to clone the repo after each commit. Setting up a bash script which allowed for Jenkins to then build a copy of the program and excecute the tests and output a coverage report at the end.
![Jenkins1](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/jenkis%20code.png)
![Jenkins2](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/Jenkins%20script.png)
The jenkins sudo chmod makes the test.sh exceuteable and in the second picture you can see the code that it runs to build and test the application.

![CiPipeline](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/cipipeline.png)
The Ci pipeline i used

##Testing
As mentioned previously the testing was automated by Jenkins. It is a key part of the CI pipeline and i implemented unit testing for this project.
Unit testing i did went along and tested the key aspects of my program being the create, read, update and delete.  Jenkins then outputted a a coverage report (see below) of how the tests went.

![tests](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/Coverage%20report.png)
As seen on the coverage report i have not been able to hit the 100% tests on the route.py This is due to some over complicated code i have written that is hard to tell the system to follow and currently under the time constraints i have been unable to resolve. It is currently in the in progress section of my Jira board due to this. While i am able to produce results manually when i use the program i am unsure why the tests to not function as intended.

## The App

###Registration 
![Registration](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/registration.png)
The registration page allows users to create a User.

![Login](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/login.png)
The login page reads the user database and possibly allows the user to log in if there username and password is found

![Home](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/home.png}
The home page allows the user to access each of the other pages of the app

![Save](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/save.png)
The save page creates a entry for a correct word and for a set of guesses.

![Stats](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/stats.pn)
The stats page automatically looks up the users most used word on load and allows for the user to look up how much they have used other words.

![Update](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/update.png)
The update page allows users to change the entry they put in for a guess that coresponds to a correct word

![Delete](https://github.com/QAEdd/Wordle-Project/blob/main/wordleproj/delete.png)
The delete page allows the user to delete the entry they have associated with a correct word.


## What went wrong 

During the programming i came across several issues. I have already referenced the biggest one of having the users information stored in plain text during the risk assessment. Another during the testing phase of not being able to get a test the full coverage of my program. Throughout the program i did experience small hurdles one of which caused me to update my ERD to allow for a logged user database. 

### Possible improvements
The scope of what i orginally planned was definetly outside of the scope of what i thought i could get done as i would have like for a must more detailed stats page that allowed the user to get a big breakdown of they're wordle stats. In the far future i would also like an automated save function that either would work off a screenshot or linked to the app itself that saves the user having to manually input the data. This is currently outside of my skill set and i may return once i have improved my programming abilities to try and implement it.

