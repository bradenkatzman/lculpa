from flask import Flask, render_template, request, redirect
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config['DEBUG'] = True

# MongoDB Config
app.config['MONGODB_SETTINGS'] = {
     'host': 'mongodb://localhost/lculpa'
}

# Create database connection object
db = MongoEngine(app)

class Review(db.Document):
    name = db.StringField(required=True)
    department = db.StringField(required=True)
    classes = db.StringField(required=True)
    summary = db.StringField(required=True)
    workload = db.StringField(required=True)

@app.route("/submitreview", methods=['GET', 'POST'])
def review():
	if request.method == 'POST':
		name = request.form["name"]
		department = request.form["department"]
		classes = request.form["classes"]
		summary = request.form["summary"]
		workload = request.form["workload"]
		review = Review(name=name, department=department, classes=classes,
			summary=summary, workload=workload)
		review.save()
		return redirect("/completedreview")
	return render_template('home.html', reviews=Review.objects)


@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
	strrequest = str(request)
	print strrequest
	searchKey, garbage = (strrequest[47:]).split('\'')
	searchKey = searchKey.replace("+", " ")
	nameresults = Review.objects(name=searchKey)
	classesresults = Review.objects(classes=searchKey)
	departmentresults = Review.objects(department=searchKey)
	return render_template('results.html', nameresults=nameresults, 
		departmentresults=departmentresults, classesresults=classesresults)

@app.route('/goldbush', methods=['GET'])
def goldbush():
	kohnreviews = Review.objects(name="Shira Kohn")
	androphyreviews = Review.objects(name="Ron Androphy")
	gampelreviews = Review.objects(name="Benjamin R. Gampel")
	return render_template('goldbush.html', kohnreviews=kohnreviews, 
		androphyreviews=androphyreviews, gampelreviews=gampelreviews)

@app.route('/silverbush', methods=['GET'])
def silverbush():
	kalmanofskyreviews = Review.objects(name="Amy Kalmanofsky")
	return render_template('silverbush.html', kalmanofskyreviews=kalmanofskyreviews
		)

@app.route("/completedreview", methods=['GET'])
def completed():
	return render_template('completedreview.html')

@app.route("/contact", methods=['GET'])
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
    app.run()