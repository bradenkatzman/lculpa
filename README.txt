README.txt


MY FIRST WEB APP!

This is my first web application. It's a professor review website that allows students at my college to review professors, and look up review for classes they may be interested in taking. I wrote this application in python, using flask. I made a review class that contains all the necessary information (in app.py) and users fill out a form (home.html) that creates this review object and saves instances of them in a MongoDB. I'm currently hosting the app on heroku, running an instance of the database on the backend through MongoLab. The code is open source so check it out! I used Python, HTML, and CSS, with Flask, MongoDB, and Bootstrap.

____________________________________________________________________

(in LCULPA directory: start virtualenv)
$ . env/bin/activate

$ deactivate

    -- after starting database using mongod -->
$ python app.py


(on new terminal window):

$ mongod


(on new terminal window):

check database:

$ mongo
> use lculpa
switched to db lculpa
> db.review.find()

(pushing commits to github - post commit)
$ git push -u origin master
