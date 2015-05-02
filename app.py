from flask import Flask, render_template, request, redirect
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config['DEBUG'] = True

# MongoDB Config
app.config['MONGODB_SETTINGS'] = {
    # 'host': "mongodb://admin:columbia@ds029051.mongolab.com:29051/exchangeatcu"
     'host': 'mongodb://localhost/lculpa'
}

# Create database connection object
db = MongoEngine(app)

class Review(db.Document):
    name = db.StringField(required=True)

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		name = request.form["review"]
		review = Review(name=name)
		review.save()
		return redirect("/")
	return render_template('home.html', reviews=Review.objects)


if __name__ == "__main__":
    app.run()