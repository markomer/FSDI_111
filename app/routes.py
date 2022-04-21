from flask import Flask   # from the flask module import the Flask class


app = Flask(__name__)     # Create an instance of "Flask"


@app.get("/")             # Flask decorator that allows us to ma "/" to "index"
                          # Python function - in Flask this is a "view function"
                          # Python dictionary containing key-value pairs
def index():
  me = {
    "first_name": "Mark",
    "last_name": "Omer",
    "hobbies": "Art Stuff",
    "active": True
  }
  return me               # return statement flask converts dict to JSON