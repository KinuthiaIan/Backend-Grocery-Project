from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# This is the users table
class Users(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.Integer)
    last_name = db.Column(db.String)
    email = db.Column(db.Integer, unique=True)
    password_hash = db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# The authenticate table
class Authenticate(db.Model, SerializerMixin):
    __tablename__ = "authenticate"

    id = db.Column(db.Integer, primary_key=True)

    user_email = db.Column(db.String, db.ForeignKey('users.email'))
    user_password = db.Column(db.String, db.ForeignKey('users.password_hash'))

# The products table
class Products(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)

    price = db.Column(db.Float)
    image = db.Column(db.String)
    name = db.Column(db.String)
    category = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('authenticate.id'))