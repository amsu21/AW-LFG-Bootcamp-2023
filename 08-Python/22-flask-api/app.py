from flask import Flask, render_template

app = Flask(__name__)

# GET ROUTE
@app.route('/')
def index():
    print("FOUND THE FILE!!!")
    return render_template('index.html')

app.run(port=8080, debug=True)