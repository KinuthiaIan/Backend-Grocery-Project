from flask import Flask
from flask_migrate import Migrate

from models import db, User, Authenticate, Product


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)





db.init_app(app)
@app.route('/')
def hello():
    return f"<h1>Let's Gooooooo!</h1>"


# @app.route('/products/<string:category_name>')
# def get_product_by_category(category_name):
#     products = []
#     for product in Product.query.filter(Product.category == category_name).all():
#         product_dict = {
#             "id":product.id,
#             "name":product.name,
#             "price":product.price,
#             "description":product.description,
#         }
#         products.append(product_dict)

#     response = make_response(
#         products,
#         200,
#         {"Content-Type": "application/json"}
#     )
if __name__ == '__main__':
    app.run(port=5555, debug=True)