from flask import Flask, request
from flask import render_template, jsonify
import re
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/check', methods=['POST'])
def check():

    sprawdz = request.form['name']

    if re.match("\d{2}-\d{3}$", sprawdz) :
        return jsonify({'name' : 'Prawidłowy kod!'})
    else:
        return jsonify({'error' : 'Nieprawidłowy kod...'})

if __name__ == '__main__':
    app.run(debug=True)