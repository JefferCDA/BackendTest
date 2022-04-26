from utils.config import db, ma
from datetime import datetime

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    clientName = db.Column(db.String(100))
    dateTime = db.Column(db.DateTime, default=datetime.now())
    productId = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer)
    clientAddress = db.Column(db.String(50))
    city = db.Column(db.String(30))
    clientPhone = db.Column(db.String(20))
    state = db.Column(db.String(15))
    stateDate = db.Column(db.DateTime)

    def __init__(self,clientName, dateTime, productId, quantity, clientAddress, city,clientPhone,state, stateDate):
        self.clientName = clientName
        self.dateTime = dateTime
        self.productId = productId
        self.quantity = quantity
        self.clientAddress = clientAddress
        self.city = city
        self.clientPhone = clientPhone
        self.state = state
        self.stateDate = stateDate
        
class OrdersSchema(ma.Schema):
    class Meta():
        fields = ('id', 'clientName', 'dateTime', 'productId', 'quantity','clientAddress','city', 'clientPhone', 'state' , 'stateDate')