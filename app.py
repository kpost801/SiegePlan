#from flask import Flask, render_template, jsonify
from core import create_app
from livereload import Server
from dotenv import load_dotenv
import os

load_dotenv(override=True)

environment = os.getenv("ENV", "production")

app = create_app(environment)


if __name__ == "__main__":
	if environment == "development":
		server = Server(app.wsgi_app)
		server.watch("core/**/*.py")
		server.watch("core/**/*.html")
		server.watch("core/**/*.css")
		server.serve(port=5000)  # Start the server with livereload
	else:
    	# Run in standard mode for production
		app.run(port=5000)