from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

# route variables
@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)

@app.route('/stats')
def stats():
    data = {
        "Chicken": 76,
        "Computer Science (Major)": 11,
        "Computer Science (Special)": 37,
        "Fish": 6,
        "Information Technology (Major)": 26,
        "Information Technology (Special)": 18,
        "Vegetable": 10
    }
    return jsonify(data)

@app.route('/add/<float:a>/<float:b>')
def add(a, b):
    return jsonify(result=a + b)

@app.route('/subtract/<float:a>/<float:b>')
def subtract(a, b):
    return jsonify(result=a - b)

@app.route('/multiply/<float:a>/<float:b>')
def multiply(a, b):
    return jsonify(result=a * b)

@app.route('/divide/<float:a>/<float:b>')
def divide(a, b):
    if b == 0:
        return jsonify(error="Cannot divide by zero"), 400
    return jsonify(result=a / b)



app.run(host='0.0.0.0', port=8080, debug=True)
