"""basic flask APP"""
from flask import Flask, render_template, Blueprint
from places import places

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(places, url_prefix='places')

@app.errorhandler(404)
def not_found(error):
    """error handler"""
    return render_template('404.html')


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])

def home():
    """home route"""
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    """about route"""
    return render_template('about.html')

@app.route('/discover', methods=['GET'])
def discover():
    """discover route"""
    return render_template('discover.html')

@app.route('/places', methods=['GET'])
def place():
    """place route"""
    return render_template('places.html')

if __name__ == '__main__':
    app.run()
