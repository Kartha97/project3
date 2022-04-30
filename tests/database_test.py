import os

from click.testing import CliRunner

from app.db.models import User
from app import create_database
from app.db import db

from werkzeug.security import generate_password_hash

runner = CliRunner()

def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True

def test_create_database_upload_folder():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../app/uploads')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True

def test_db_storing(application):
    with application.app_context():
        # checking there are no users
        assert db.session.query(User).count() == 0
        # showing how to add a record
        # create a record
        user = User('test1@gmail.com', 'testtest')
        # add it to get ready to be committed
        db.session.add(user)

        user = User.query.filter_by(email='test1@gmail.com').first()

        # asserting that the user retrieved is correct which tells that it is being stored
        assert user.email == 'test1@gmail.com'
        db.session.commit()

        # Validating there is one value in user db
        assert db.session.query(User).count() == 1
        # deleting user

        db.session.delete(user)
        # Validating that user is deleted or not
        assert db.session.query(User).count() == 0


