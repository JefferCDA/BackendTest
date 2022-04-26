from datetime import datetime
from flask import Blueprint, request
from models.orders import Orders, OrdersSchema
from utils.config import db

orderRoutes= Blueprint('orders',__name__)

orderSchema = OrdersSchema()
ordersSchema = OrdersSchema(many=True)

@orderRoutes.route('/orders', methods=['POST'])
def setOrder():
    clientName = request.json['clientName']
    dateTime = datetime.now()
    productId = request.json['productId']
    quantity = request.json['quantity']
    clientAddress = request.json['clientAddress']
    city = request.json['city']
    clientPhone = request.json['clientPhone']
    state = 'En espera'
    stateDate = datetime.now()

    newOrder = Orders(clientName, dateTime,productId ,quantity, clientAddress, city, clientPhone, state, stateDate)

    db.session.add(newOrder)
    db.session.commit()    

    return orderSchema.jsonify(newOrder)

@orderRoutes.route('/orders', methods=['GET'])
def getOrders():
    
    allOrders = Orders.query.all()
    result = ordersSchema.dump(allOrders)

    return ordersSchema.jsonify(result)

@orderRoutes.route('/orders/<id>', methods=['GET'])
def getOrder(id):
    order = Orders.query.get(id)

    return orderSchema.jsonify(order)

@orderRoutes.route('/orders/<id>', methods=['PUT'])
def changeOrderState(id):
    order = Orders.query.get(id)
    state = request.json['state']
    stateDate = datetime.now()
    
    order.state = state
    order.stateDate = stateDate
    db.session.commit()

    return orderSchema.jsonify(order)