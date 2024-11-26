from datetime import datetime
from . import db  # Importamos la instancia db desde __init__.py

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    correo = db.Column(db.String(100), unique=True)
    telefono = db.Column(db.String(20))
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    # Relaciones
    direcciones = db.relationship('Direccion', backref='cliente', lazy=True)
    pagos = db.relationship('Pago', backref='cliente', lazy=True)

class Comida(db.Model):
    id_comida = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float)
    categoria = db.Column(db.String(50))
    imagen = db.Column(db.String(255))

class Direccion(db.Model):
    id_direccion = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    direccion = db.Column(db.String(255))
    ciudad = db.Column(db.String(100))
    codigo_postal = db.Column(db.String(10))
    pais = db.Column(db.String(50))

class Pago(db.Model):
    id_pago = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    metodo_pago = db.Column(db.String(50))
    monto = db.Column(db.Float)
    estado_pago = db.Column(db.String(20))
    fecha_pago = db.Column(db.DateTime, default=datetime.utcnow)

class Total(db.Model):
    id_total = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    id_pago = db.Column(db.Integer, db.ForeignKey('pago.id_pago'), nullable=False)
    total = db.Column(db.Float)