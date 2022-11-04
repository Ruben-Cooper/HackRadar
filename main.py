from hackathon import create_app
from flask_sqlalchemy import SQLAlchemy


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
