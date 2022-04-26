from utils.config import db, ma

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))

    def __init__(self,name,price,description):
        self.name = name
        self.price = price
        self.description = description

class ProductsSchema(ma.Schema):
    class Meta():
        fields = ('id','name','price','description')