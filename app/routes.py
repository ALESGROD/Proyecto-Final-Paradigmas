from flask import Blueprint, render_template, request
from app import db
from app.models import Cliente  # Importa el modelo Cliente si lo necesitas

# Definir el Blueprint "main"
main = Blueprint('main', __name__)

# Datos de menú
menu = {
    "Foods": [
        {"name": "Salad", "price": 3.5, "image": "salad.jpg"},
        {"name": "Japanese Noodles", "price": 4.5, "image": "noodles.jpg"},
        {"name": "Spaghetti", "price": 3.7, "image": "spaghetti.jpg"}
    ],
    "Drinks": [
        {"name": "Raspberry", "price": 3.5, "image": "raspberry.jpg"},
        {"name": "Chocolate Pudding", "price": 4.5, "image": "pudding.jpg"}
    ],
    "Desserts": [
        {"name": "Strawberry Cake", "price": 2.5, "image": "strawberry_cake.jpg"},
        {"name": "Chocolate Cake", "price": 3.0, "image": "chocolate_cake.jpg"}
    ]
}

# Crear las rutas
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/menu')
def menu_page():
    return render_template('menu.html', menu=menu)

@main.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']

        # Crear un nuevo cliente y agregarlo a la base de datos
        nuevo_cliente = Cliente(nombre=nombre, correo=correo, telefono=telefono)
        db.session.add(nuevo_cliente)
        db.session.commit()
        
        return redirect(url_for('main.index'))  # Redirige al inicio después de agregar

    return render_template('form.html')  # Muestra el formulario si es GET
