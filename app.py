from flask import Flask, render_template

# This sets up the Flask app so you can define routes and handle requests.
app = Flask(__name__)  

# This defines the main route for the application. Routes map URLs to specific code.
@app.route("/")  
def hello():

	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)  