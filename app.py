# app.py

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
# def index():
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # freezer.freeze()
    app.run(debug=True)