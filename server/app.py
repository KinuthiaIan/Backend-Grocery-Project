from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, Product
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity,create_access_token
import datetime
from bcrypt import checkpw

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["JWT_SECRET_KEY"] = 'your-secret-key'  
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

db.init_app(app)
api = Api(app)

@app.route('/')
def index():
    return f"<h1>Grocery Store RESTful API</h1>"


    


class Products(Resource):
    def get(self):
        data = []
        for product in Product.query.all():
            product_dict = product.to_dict()

            data.append(product_dict)

        response = make_response(data, 200)

        return response
    
    def post(self):
        data=request.get_json()
        
        new_product = Product(
            category=data['category'],
            description=data['description'],
            image=data['image'],
            name=data['name'],
            price=data['price'],
            quantity=data['quantity']
            )
        
        db.session.add(new_product)
        db.session.commit()
        
        return make_response(new_product.to_dict(),201)
    
    
api.add_resource(Products, '/products')




@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], gmail=data['gmail'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user:
        token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=1))
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401



if __name__ == '__main__':
    app.run(port=5555, debug=True)