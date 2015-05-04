from flask import Flask, render_template, request, redirect
from flask.ext.mongoengine import MongoEngine
import os

app = Flask(__name__)

app.config['DEBUG'] = True

if "MONGODB_HOST" in os.environ:
	app.config['MONGODB_HOST'] = os.environ['MONGODB_HOST']
else:
	host = 'localhost'

if "MONGODB_PORT" in os.environ:
	app.config['MONGODB_PORT'] = os.environ['MONGODB_PORT']
else:
	port = 27017

if "MONGODB_USERNAME" in os.environ:
	app.config['MONGODB_USERNAME'] = os.environ['MONGODB_USERNAME']


if "MONGODB_PASSWORD" in os.environ:
	app.config['MONGODB_PASSWORD'] = os.environ['MONGODB_PASSWORD']

app.config['MONGODB_DB'] = 'lculpa'



# Create database connection object
db = MongoEngine(app)

# Review Object
class Review(db.Document):
    name = db.StringField(required=True)
    department = db.StringField(required=True)
    classes = db.StringField(required=True)
    summary = db.StringField(required=True)
    workload = db.StringField(required=True)

@app.route("/submitreview", methods=['GET', 'POST'])
def review():
	if request.method == 'POST':
		
		# grab data from form
		name = request.form["name"]
		department = request.form["department"]
		classes = request.form["classes"]
		summary = request.form["summary"]
		workload = request.form["workload"]
		
		# create and save new review object
		review = Review(name=name, department=department, classes=classes,
			summary=summary, workload=workload)
		review.save()

		# redirect to completed page
		return redirect("/completedreview")
	
	# if HTTP method is 'GET', return submission form
	return render_template('home.html', reviews=Review.objects)

# home page
@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
	#  cast request to string to parse for search key
	strrequest = str(request)
	
	# 47:end is search key through end of string, then split key
	# to get rid of string past search
	searchKey, garbage = (strrequest[54:]).split('\'')
	
	# replace + with space
	searchKey = searchKey.replace("+", " ")
	
	# search database using searchKey
	nameresults = Review.objects(name=searchKey)
	classesresults = Review.objects(classes=searchKey)
	departmentresults = Review.objects(department=searchKey)
	
	# return results.html and cursor objects to loop through and print
	return render_template('results.html', nameresults=nameresults, 
		departmentresults=departmentresults, classesresults=classesresults)

@app.route('/goldbush', methods=['GET'])
def goldbush():
	# search database for gold professors
	kohnreviews = Review.objects(name="Shira Kohn")
	androphyreviews = Review.objects(name="Ron Androphy")
	gampelreviews = Review.objects(name="Benjamin R. Gampel")
	
	# return goldbush.html and cursor objects to gold professors
	return render_template('goldbush.html', kohnreviews=kohnreviews, 
		androphyreviews=androphyreviews, gampelreviews=gampelreviews)

@app.route('/silverbush', methods=['GET'])
def silverbush():
	# search database for silver professors
	kalmanofskyreviews = Review.objects(name="Amy Kalmanofsky")
	
	# return silverbush.html and cursor objects to silver professors
	return render_template('silverbush.html', kalmanofskyreviews=kalmanofskyreviews)

@app.route("/completedreview", methods=['GET'])
def completed():
	return render_template('completedreview.html')

@app.route("/contact", methods=['GET'])
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
    app.run()