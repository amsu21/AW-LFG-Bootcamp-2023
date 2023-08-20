from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

bugs = []

# GET ROUTE
# @app.route('/bugs', methods=['GET'])
# def getBugs():
#     print("TEMPLATE RENDERED")
#     return render_template('bugs.html')

@app.route('/bugs', methods=['GET'])
def getBug():
    bugs = {"id" : "1", "title" : "App not working", "createdAt" : "3:00", "isClosed" : "True"}
    print("BUGS DATA")
    print()
    print(bugs)
    print()
    return jsonify(bugs)

# POST ROUTE
@app.route('/bugs', methods=['POST'])
def postBugs():
    bugs = []
    newBug = {"id" : "2", "title" : "Pasword Reset", "createdAt" : "1:00", "isClosed" : "False"}
    allBugs = bugs.append(newBug)
    print("BUGS DATA POST REQ")
    print("**************************")
    print()
    print(allBugs)
    print()
    return jsonify(allBugs)


app.run(port=3000, debug=True)