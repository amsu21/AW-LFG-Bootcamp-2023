from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# GET ROUTE
@app.route('/', methods=['GET'])
def index():
    # print("FOUND THE FILE!!!")
    # return render_template('index.html')
    data = {"name" : "Amsu"}
    print("JSON DATA")
    print(data)
    return jsonify(data)

# POST ROUTE
@app.route('/', methods=['POST'])
def post_index():
    data = {"req-method" : "POST", "name" : "Amsu"}
    print("JSON DATA POST REQ")
    print()
    print(data)
    print()
    return jsonify(data)

# ROUTE PARAMS
@app.route('/greet', methods=["POST"])
def greet():
    req_payload = request.get_json()
    res_payload = {"message" : f"Hi {req_payload['name']}, Have a good one!!!!"}
    return jsonify(res_payload)


@app.route('/greet/<string:username>', methods=['GET'])
def greetParam(username):
    res_payload = { "message" : f"Wassup {username}, Have a good day!!!"}
    print(res_payload)
    return jsonify(res_payload)
    
    
@app.route("/bugs/<int:id>/<string:name>", methods=["GET"])
def get_Bug_By_Id(id, name):
    print(id, name)
    return "thank you"

app.run(port=8080, debug=True)