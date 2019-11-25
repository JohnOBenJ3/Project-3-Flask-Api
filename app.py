import os
from flask import Flask, jsonify, g
import models
from flask_login import LoginManager
from flask_cors import CORS
from resources.animals import animal
from resources.shelters import shelter
from resources.admin import admin


DEBUG = True #I don't want any errors but when I get them I want them to be better
PORT = 8000 #localhost 8000

# This initializes Flask
app = Flask(__name__) # __name__ == "__main__"
app.secret_key = 'asldn;alisdngl;asdnl;kadsnalksdnglkasdn'

login_manager = LoginManager() #<-- apparently you need these parentheses
login_manager.init_app(app)

@login_manager.user_loader
def load_user(adminid):
  try: 
    return models.Admin.get(models.Admin.id == adminid)
  except models.DoesNotExist:
    return None
  
@login_manager.unauthorized_handler
def unauthorized():
  return jsonify(data={'ERROR'}, status={'code': 401,'message': "This is a restricted area."})

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
