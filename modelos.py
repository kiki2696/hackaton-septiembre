from flask_sqlalchemy import SQLAlchemy


# crear objeto SQLAlchemy
db = SQLAlchemy()

### MODELOS ###

# Crear modelo de Ciudad
class Universidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    universidad = db.Column(db.String(100), nullable=False)
    # relaciones con otras tablas
    parada = db.relationship('Parada', backref='universidad', lazy=True)
    bus = db.relationship('Bus', backref='universidad', lazy=True)

# Crear modelo de Parada
class Parada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parada = db.Column(db.String(100), nullable=False)
    latitud = db.Column(db.String(100), nullable=False)
    longitud = db.Column(db.String(100), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    # relacion parada con horario
    horario = db.relationship('Horario', backref='parada', lazy=True)
    # relacion parada con bus
    bus = db.relationship('Bus', backref='parada', lazy=True)
    # relacionamos parada con universidad
    universidad_id = db.Column(db.Integer, db.ForeignKey('universidad.id'), nullable=False)

  

# Crear modelo de Horario
class Horario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turno = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.String(100), nullable=False)
    # relacion horario con bus
    bus = db.relationship('Bus', backref='horario', lazy=True)
    # relacionamos parada con ciudad
    parada_id = db.Column(db.Integer, db.ForeignKey('parada.id'), nullable=False)

# Crear modelo de Bus
class Bus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus = db.Column(db.String(100), nullable=False)
    chapa = db.Column(db.String(100), nullable=False)
    # relacionamos bus con ciudad
    universidad_id = db.Column(db.Integer, db.ForeignKey('universidad.id'), nullable=False)
    parada_id = db.Column(db.Integer, db.ForeignKey('parada.id'), nullable=False)
    horario_id = db.Column(db.Integer, db.ForeignKey('horario.id'), nullable=False)


    