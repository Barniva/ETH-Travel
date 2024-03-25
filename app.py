"""Ethio-Travel flask APP"""
from flask import Flask, render_template, jsonify


"""declare app variable"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.errorhandler(404)
"""404 error handler"""
def not_found(error):
    return render_template('404.html')


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
"""home route"""
def home():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
"""about route"""
def about():
    return render_template('about.html')


@app.route('/discover', methods=['GET'])
"""discover route"""
def discover():
    return render_template('discover.html')


@app.route('/places', methods=['GET'])
"""place route"""
def place():
    return render_template('places.html')


@app.route('/place1', methods=['GET'])
"""place1 route"""
def place1():
    return render_template('place1.html')


@app.route('/place2', methods=['GET'])
"""place2 route"""
def place2():
    return render_template('place2.html')


@app.route('/place3', methods=['GET'])
"""place3 route"""
def place3():
    return render_template('place3.html')


@app.route('/place4', methods=['GET'])
"""place4 route"""
def place4():
    return render_template('place4.html')


@app.route('/place5', methods=['GET'])
"""place5 route"""
def place5():
    return render_template('place5.html')


if __name__ == '__main__':
    app.run()