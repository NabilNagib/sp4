import os
from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    def to_dict(self, include_hero_powers=False):
        data = {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
        }
        if include_hero_powers:
            data['hero_powers'] = [hero_power.to_dict() for hero_power in self.hero_powers]
        return data

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength,
            'hero': self.hero.to_dict(),
            'power': self.power.to_dict()
        }

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'This is an API for tracking heroes and their superpowers.'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict(include_hero_powers=True))
    else:
        return jsonify({"error": "Hero not found"}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    else:
        return jsonify({"error": "Power not found"}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)

    if power is None:
        response_body = {
            "error": "Power not found"
        }
        response = make_response(response_body, 404)
        return response

    else:
        data = request.get_json()
        if "description" in data:
            power.description = data["description"]
            db.session.commit()
            response_body = {
                "description": power.description,
                "id": power.id,
                "name": power.name
            }
            response = make_response(response_body, 200)
            return response
        else:
            response_body = {
                "errors": ["validation errors"]
            }
            response = make_response(response_body, 400)
            return response
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    if request.method == 'POST':
        data = request.get_json()
        hero_id = data.get("hero_id")
        power_id = data.get("power_id")
        strength = data.get("strength")

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero or not power:
            response_body = {
                "errors": ["Hero or Power not found"]
            }
            response = make_response(response_body, 404)
            return response

        if not strength:
            response_body = {
                "errors": ["Strength is required"]
            }
            response = make_response(response_body, 400)
            return response

        hero_power = HeroPower(hero=hero, power=power, strength=strength)
        db.session.add(hero_power)
        db.session.commit()

        hero_power_data = {
            "id": hero_power.id,
            "hero_id": hero_power.hero_id,
            "power_id": hero_power.power_id,
            "strength": hero_power.strength,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": {
                "description": power.description,
                "id": power.id,
                "name": power.name
            }
        }

        response = make_response(hero_power_data, 201)
        return response

if __name__ == '__main__':
    app.run(port=5555, debug=False)
