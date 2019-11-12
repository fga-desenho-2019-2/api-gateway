from flask.cli import FlaskGroup
from flask_cors import CORS
from flask_script import Manager
from project import create_app

app = create_app()
CORS(app)

cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    cli()