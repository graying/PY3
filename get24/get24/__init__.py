# from flask import Flask
#
# # from cal_24 import cal24
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return "get 24 index"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

import os

from flask import Flask, redirect


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'get24.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # redirect '/' to '/input' page 127.0.0.1:5000-> 127.0.0.1:5000/input
    @app.route('/')
    def hello():
        return redirect('/input')

    from . import input
    app.register_blueprint(input.bp)

    return app
