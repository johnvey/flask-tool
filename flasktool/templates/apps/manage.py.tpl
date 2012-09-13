#!/usr/bin/env python
from __future__ import absolute_import

from flask.ext.script import Manager, Server
{% if app.layout == 'factory' %}
from {{app.package_name}} import create_app
app = create_app()
{% else %}
from app import app
{% endif %}

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0'))

if __name__ == "__main__":
    manager.run()
