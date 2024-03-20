"""basic flask APP"""
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.url_map.strict_slashes = False
@app.errorhandler(404)
def error():
    return jsonify({'404: Page Not Found'})


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])

def home():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/discover', methods=['GET'])
def discover():
    return render_template('discover.html')

@app.route('/places', methods=['GET'])
def place():
    return render_template('places.html')

if __name__ == '__main__':
    app.run(debug=True)