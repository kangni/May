# -*- coding: utf-8 -*-
import os
from flask.ext.script import Manager, Server
from May.models import db, User, Post, Tag, Comment
from May import create_app
from flask.ext.migrate import Migrate, MigrateCommand

env = os.environ.get('MAY_ENV', 'dev')
app = create_app('May.config.%sConfig' % env.capitalize())

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Tag=Tag, Comment=Comment)

if __name__ == '__main__':
    manager.run()
