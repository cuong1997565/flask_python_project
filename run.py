from app import app,db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migrate = Migrate(app, db)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)