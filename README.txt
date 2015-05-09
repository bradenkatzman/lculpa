Braden Katzman - LCULPA Web App - README.txt


MY FIRST WEB APP!

This is my first web app. It's a professor review website that allows students at my college to review professors, and look up reviews for classes they may be interested in taking. I wrote this application in Python, using Flask. I made a review class that contains all the necessary information (in app.py) and users fill out a form (home.html) that creates this review object and saves instances of them in a MongoDB. I'm currently hosting the app on heroku, running an instance of the database on the backend through MongoLab. The code is open source so check it out! I used Python, HTML, and CSS, with Flask, MongoDB, and Bootstrap.

Check out the app here:
lculpa.herokuapp.com

____________________________________________________________________

(in LCULPA directory: start virtualenv)
$ . env/bin/activate

$ deactivate

-- after starting database using mongod --
$ python app.py


for local instance of database:
$ mongod


-- check database via MongoLab

push commits to github
$ git push -f origin master

push commits to heroku:
git push -f heroku master

start app locally:
$ foreman start

To look at all reviews, press search on empty input
