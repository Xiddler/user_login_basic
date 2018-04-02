from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////media/ubuntu/3520-FD13/2programming_repository/python/1python_projects/flask-projects/user_login_basic/database.db'
app.config['CSRF_ENABLED'] = True 
app.config['USER_ENABLE_EMAIL'] = False 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

@app.route('/')
def index():
    return '<h1>This is the home page!</h1>'

@app.route('/profile')
@login_required
def profile():
    return '<h1>This is the protected profile page!</h1>'

if __name__ == '__main__':
    app.run(debug=True) 
