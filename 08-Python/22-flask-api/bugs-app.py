""" 
bug
    - id
    - title
    - createdAt
    - isClosed

Keep the bugs in the memory
autoincrement the id for the newly created bugs (starting from 1)

expose the following end points         (response status codes)
GET - http://localhost:8080/bugs        (200)
GET - http://localhost:8080/bugs/100    (200/404)
POST - http://localhost:8080/bugs       (201)
PUT - http://localhost:8080/bugs/100    (200/404)
DELETE - http://localhost:8080/bugs/100 (200/404)

Investigate how to send the appropriate status code as response
"""

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

bugs = [
    {
        'id' : 1,
        'name' : 'Bug - 1',
        'isClosed' : False
    },
    {
        'id': 2,
        'name': 'Bug - 2',
        'isClosed': True
    },
    {
        'id': 3,
        'name': 'Bug - 3',
        'isClosed': False
    }
]

@app.route('/')
def home():
    #return "Hi there!"
    return render_template('index.html')

@app.route('/bugs', methods=['GET'])
def get_bugs():
    print("ALL DA BUGS")
    print()
    print(bugs)
    return jsonify(bugs)

@app.route('/bugs', methods=['POST'])
def save_new_bug():
    request_data = request.get_json()
    new_bug_id = max(bug['id'] for bug in bugs) + 1
    new_bug = {
        'id' : new_bug_id,
        'name' : request_data['name'],
        'isClosed' : request_data['isClosed']
    }
    bugs.append(new_bug)
    return new_bug, 201


@app.route('/bugs/<int:id>', methods=['PUT'])
def update_bug(id):
    updated_bug = request.get_json()
    for bug in bugs:
        if bug['id'] == id:
            bug['name'] = updated_bug['name']
            bug['isClosed'] = updated_bug['isClosed']
            return updated_bug
    return {"message" : "bug not found"}, 404    


@app.route('/bugs/<int:id>', methods=['DELETE'])
def delete_bug(id):
    for bug in bugs:
        if bug['id'] == id:
            bugs.remove(bug)
            return {}
    return {"message": "bug not found"}, 404

@app.route('/bugs/<int:id>')
def get_a_bug(id):
    for bug in bugs:
        if bug['id'] == id:
            return bug
    return {"message" : "bug not found"}, 404

#comment

app.run(port=5000, debug=True)