from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)

def create_db():
        with app.app_context():
            db.create_all()

create_db()

# Function to check if name and email are strings and age is a number
def parameter_check(name, age, email):
    if not isinstance(name, str):
        return jsonify({"error": "Name should be a string"}), 400
    elif not isinstance(email, str):
        return jsonify({"error": "Email should be a string"}), 400
    try:
        age = int(age)
    except ValueError:
        return jsonify({"error": "Age should be a number"}), 400


@app.route('/api', methods=['POST'])
def create():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    # Check if name and email are strings and age is a number
    parameter_check(name, age, email)
    # Create user
    user = User(name=name, age=age, email=email)
    # Check if email already exists
    try:
        db.session.add(user)
        db.session.commit()
    except SQLAlchemyError as e:
        if 'UNIQUE constraint failed' in str(e):
            return jsonify({"error": "Email already exists"}), 400
    return jsonify( success= {
        'success': 'User created successfully!',
        'name': name,
        'age': age,
        'email': email
    })


@app.route('/api/<int:user_id>', methods=['GET'])
def read(user_id):
    user = db.session.query(User).get(user_id)
    if user == None:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify({
        'id': user.id,
        'name': user.name,
        'age': user.age,
        'email': user.email
    })
     
@app.route('/api/<int:user_id>', methods=['PATCH'])
def update(user_id):
    user = db.session.query(User).get(user_id)
    if user == None:
        return jsonify({"error": "User not found"}), 404
    # Check if name and email are strings
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    parameter_check(name, user.age, email) 
    # Update user
    user.name = name
    user.email = email
    user.age = age
    db.session.commit()
    return jsonify({
        'success': 'User updated successfully!',
        'id': user.id,
        'name': user.name,
        'age': user.age,
        'email': user.email
    })

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    user = db.session.query(User).get(user_id)
    if user == None:
        return jsonify({"error": "User not found"}), 404
    # Delete user
    db.session.delete(user)
    db.session.commit()
    return jsonify({"success": "User deleted successfully!"})


if __name__ == '__main__':
    
    app.run(debug=True)