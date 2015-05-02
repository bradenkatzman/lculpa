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

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		name = request.form["name"]
		department = request.form["department"]
		classes = request.form["classes"]
		summary = request.form["summary"]
		workload = request.form["workload"]

		review = Review(name=name, department=department, classes=classes,
			summary=summary, workload=workload)
		review.save()
		return redirect("/")
	return render_template('home.html', reviews=Review.objects)


if __name__ == "__main__":
    app.run()