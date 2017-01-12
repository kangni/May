# -*- coding: utf-8 -*-
from flask import Flask

from models import db
from controllers.main import main_blueprint
from controllers.blog import blog_blueprint
from May.extensions import bcrypt


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(blog_blueprint)

    return app

if __name__ == '__main__':
    app = app = create_app('project.config.ProdConfig')
    app.run()
