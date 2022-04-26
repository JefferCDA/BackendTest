from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from utils.config import db
from routes.products import productsRoutes
from routes.orders import orderRoutes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:meinsm@localhost/prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)
Marshmallow(app)

with app.app_context():
    db.create_all()

app.register_blueprint(productsRoutes)
app.register_blueprint(orderRoutes)

if __name__ == '__main__':
    app.run(debug=True)