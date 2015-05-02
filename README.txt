README.txt


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
