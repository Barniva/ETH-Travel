"""places blueprint"""
from flask import Blueprint, render_template

places = Blueprint('places', __name__)


@places.route('/place1', methods=['GET'])
def place1():
    """place1 route"""
    return render_template('place1.html')


@places.route('/place2', methods=['GET'])
def place2():
    """place2 route"""
    return render_template('place2.html')


@places.route('/place3', methods=['GET'])
def place3():
    """place3 route""" 
    return render_template('place3.html')


@places.route('/place4', methods=['GET'])
def place4():
    """place4 route""" 
    return render_template('place4.html')


@places.route('/place5', methods=['GET'])
def place5():
    """place5 route"""
    return render_template('place5.html')
