from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# This is the users table
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    # serialize_rules = ('-products.user')

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    # products = db.relationship('Product', back_populates='user', cascade='all, delete-orphan',lazy=True)


    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError('Invalid email address')
        
        return address

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.password_hash}>'

# The authenticate table
class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    serialize_rules = ('-user.products',)

    id = db.Column(db.Integer, primary_key=True)

    quantity = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    name = db.Column(db.String)
    category = db.Column(db.String)
    description = db.Column(db.String)
    # users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # user = db.relationship('User', back_populates='products',lazy=True)

    @validates('category')
    def validate_category(self, key, category):
        if not category:
            raise ValueError('Category is needed')
        
        if category not in ['vegetable', 'fruit', 'dairy', 'bakery']:
            raise ValueError('Category should be either: Vegetables, Fruits, Dairy, Bakery')
        
        return category

    def __repr__(self):
        return f'<Product {self.id}, {self.price}, {self.image}, {self.name}, {self.category}, {self.description}>'