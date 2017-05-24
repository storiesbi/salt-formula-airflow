
from __future__ import print_function

import sys

from airflow import models, settings

session = settings.Session()

key = sys.argv[1]
value = sys.argv[2]
update = eval(sys.argv[3])


def get_variable(key):
    """Returns variable from Variable or config defaults"""

    return session.query(
        models.Variable).filter_by(
        key=key).first()


def create_variable(key, value):
    """Create variable"""

    return models.Variable.set(key, value)


var = get_variable(key)

if update and var:
    if var:
        var._val = value
        session.commit()
    else:
        create_variable(key, value)
else:
    create_variable(key, value)

exit()
