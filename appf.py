from flask import Flask, request
from flask import render_template, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():

    name = request.form('name')

    if re.match("\d{2}-\d{3}$", name) :
        return jsonify({'name' : 'kod prawidlowy'})
    else:
        return jsonify({'error' : 'nieprawidlowy kod'})



if __name__ == '__main__':
    app.run(debug=True)