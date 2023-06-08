"""
This app is for trial of Flask_SQLAlchemy using flask-sqlalchemy documentation
"""

from flask import Flask, render_template, url_for, redirect, request
#from flask_sqlalchemy import SQLAlchemy
from models import db, User

# create the extension
#db = SQLAlchemy()

# create an app
app = Flask(__name__)

# Configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Initialize the app with the extension
db.init_app(app)

"""The db object gives access the db.Model class to define models,
and the db.session to execute queries
--- db object will , using db.Model, automatically generate table name to subclass name of db.Model, and
 column names, using db.Column, same as to assigned variable names
"""

"""
# define models, 'CamelCase' names will be converted to 'snake_case' table name
class User(db.Model):  # table name will be 'user'
	id = db.Column(db.Integer, primary_key=True) # column name will be 'id'
	username = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String) # column name will be 'email'
"""

with app.app_context():
	db.create_all()


@app.route("/")
def index():
	return "Thanks"


@app.route("/users")
def user_list():
	""" --- db.session.execute(db.select(...)) constructs a query to select data from database
	--- Query result will user a method 'Result.scalars()' to get list of results and
		 'Result.scalar()' for single result
	"""
	users = db.session.execute(db.select(User).order_by(User.username)).scalars()
	return render_template("user_list.html", users=users)


@app.route("/users/create", methods=["GET", "POST"])
def user_create():
	if request.method == 'POST':
	 
		user = User(
		username = request.form.get("username"),
		email = request.form.get("email")
		)
		# adds a user to the session
		db.session.add(user)
		# Remembers the user just added, to the database
		db.session.commit()
		return redirect(url_for("user_detail", id=user.id))

	return render_template("create_users.html")


@app.route("/user/<int:id>")
def user_detail(id):
	user = db.get_or_404(User, id)
	return render_template("user_detail.html", user=user)


@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
	user = db.get_or_404(User, id)

	if request.method == "POST":
		# delete the user from session
		db.session.delete(user)

		# Update the deletion of the user from the database
		db.session.commit()
		return redirect(url_for('user_list'))

	return render_template("user_delete.html", user=user)


if __name__ == '__main__':
	app.run(debug=True)

