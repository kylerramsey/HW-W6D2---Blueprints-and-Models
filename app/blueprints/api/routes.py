from flask import jsonify
from . import bp as app

@app.route('/users')
def users():
    user_dict = {
        'kyler': 'ramsey'
    }

    return jsonify(user_dict)