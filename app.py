"""basic flask APP"""
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.url_map.strict_slashes = False
@app.errorhandler(404)
def errorhj(error):
    return render_template('404.html')


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

@app.route('/place1', methods=['GET'])
def place1():
    return render_template('place1.html')

@app.route('/place2', methods=['GET'])
def place2():
    return render_template('place2.html')

@app.route('/place3', methods=['GET'])
def place3():
    return render_template('place3.html')

@app.route('/place4', methods=['GET'])
def place4():
    return render_template('place4.html')

@app.route('/place5', methods=['GET'])
def place5():
    return render_template('place5.html')


if __name__ == '__main__':
    app.run(debug=True)