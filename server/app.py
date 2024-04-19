from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Product


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
api = Api(app)
migrate = Migrate(app, db)
db.init_app(app)
@app.route('/')
def hello():
    return f"<h1>Let's Gooooooo!</h1>"

class Products(Resource):
    def get(self):
        data = []
        for product in Product.query.all():
            product_dict = product.to_dict()

            data.append(product_dict)

        response = make_response(data, 200)

        return response
    
    # def post(self):
    #     data = request.get_json()

    #     new_product = Product(
    #         quantity=data['quantity'],
    #         image=data['image'],
    #         price=data['price'],
    #         name=data['name'],
    #         category=data['category'],
    #         description=data['description'],
    #         users_id=data['users_id']
    #     )
    #     db.session.add(new_product)
    #     db.session.commit()

    #     return make_response(new_product.to_dict(), 201)

api.add_resource(Products, '/product')

if __name__ == '__main__':
    app.run(port=5555, debug=True)