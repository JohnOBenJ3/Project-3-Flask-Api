import os
from flask import Flask, jsonify, g
import models
from flask_login import LoginManager
from flask_cors import CORS
from resources.animals import animal
from resources.shelters import shelter
from resources.admin import admin


DEBUG = True #better error message
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__) # __name__ == "__main__"
app.secret_key = 'asldn;alisdngl;asdnl;kadsnalksdnglkasdn'


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


CORS(app, origins=['http://localhost:3000'], supports_credentials=True) # adding this line
CORS(animal, origins=['http://localhost:3000', 'https://cierrasreactapp.herokuapp.com'], supports_credentials=True) # adding this line

app.register_blueprint(animal, url_prefix='/api/v1/animals')
CORS(shelter, origins=['http://localhost:3000', 'https://cierrasreactapp.herokuapp.com'], supports_credentials=True) # adding this line
app.register_blueprint(shelter, url_prefix='/api/v1/shelters')
CORS(admin, origins=['http://localhost:3000'], supports_credentials=True) # adding this line
app.register_blueprint(admin, url_prefix='/api/v1/admins')

if 'ON_HEROKU' in os.environ:
    print('hitting')
    models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
