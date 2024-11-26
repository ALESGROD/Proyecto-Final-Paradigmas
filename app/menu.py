import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  

# Ventana principal
root = tk.Tk()
root.title("Menu Ordering System")
root.geometry("1000x700")

# Función para actualizar el resumen del pedido
def update_order(item, price, qty_var):
    qty = int(qty_var.get())
    if qty > 0:
        order_listbox.insert(tk.END, f"{item}\t{qty}\t${qty * price:.2f}")
        total_var.set(f"${sum_total():.2f}")

# Función para calcular el total
def sum_total():
    total = 0
    for line in order_listbox.get(0, tk.END):
        parts = line.split("\t")
        if len(parts) == 3:
            total += float(parts[2][1:])  # Extraer el precio
    return total

# Variables
total_var = tk.StringVar(value="$0.00")

# Pestañas
tab_control = ttk.Notebook(root)
foods_tab = ttk.Frame(tab_control)
drinks_tab = ttk.Frame(tab_control)
desserts_tab = ttk.Frame(tab_control)
tab_control.add(foods_tab, text="Foods")
tab_control.add(drinks_tab, text="Drinks")
tab_control.add(desserts_tab, text="Desserts")
tab_control.pack(expand=1, fill="both")

# Agregar contenido a cada pestaña
def create_tab_items(tab, items):
    for idx, (name, price, img_path) in enumerate(items):
        frame = ttk.Frame(tab)
        frame.grid(row=idx // 3, column=idx % 3, padx=10, pady=10)

        # Cargar y redimensionar la imagen
        try:
            img = Image.open(img_path)
            img = img.resize((100, 100), Image.Resampling.LANCZOS)  # Cambié ANTI_ALIAS por Resampling.LANCZOS
            photo = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")
            photo = None

        # Mostrar la imagen
        img_label = tk.Label(frame, image=photo)
        img_label.image = photo  # Mantener la referencia a la imagen
        img_label.pack()

        # Nombre del artículo
        name_label = tk.Label(frame, text=name)
        name_label.pack()

        # Controles de cantidad y precio
        qty_var = tk.StringVar(value="0")
        qty_entry = tk.Entry(frame, textvariable=qty_var, width=5)
        qty_entry.pack()

        # Botón para agregar al pedido
        add_button = tk.Button(frame, text="Add", command=lambda n=name, p=price, q=qty_var: update_order(n, p, q))
        add_button.pack()

# Datos con las rutas absolutas de las imágenes
food_items = [
    ("Chicken Rice", 12.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\chickenRice.jpg"),
    ("Japanese Pan Noodles", 10.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\JapanesePanNoodles.jpg"),
    ("Kids Spaghetti", 8.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\kids_spaghetti.jpg"),
    ("Thai Food", 15.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\thaiFood.jpg"),
    ("Vietnam Food", 14.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\vietnamFood.jpg"),
    ("Pad Thai", 13.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\PadThai.jpg"),
    ("Med Salad", 7.50, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\MedSalad.png"),
    ("Ramen Noodles", 9.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\RamenNoodles.jpg"),
    ("Spaghetti", 10.50, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\spaghetti.jpg"),
]

drink_items = [
    ("Blue Hawaiian", 7.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\blue hawailan.jpg"),
    ("Lemon Ice", 4.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\lemon ice.jpg"),
    ("Pina Colada", 6.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\Pina.jpg"),
    ("Cola", 2.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\cola.jpg"),
]

dessert_items = [
    ("Chocolate Cake", 5.00, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\chocolate cake.jpg"),
    ("Strawberry Cake", 5.50, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\strawberry cake.jpg"),
    ("Chocolate Pudding", 3.50, r"C:\Users\alexd\Desktop\ProyectoFinalParadigmas\ProyectoFinalParadigmas\static\images\chocalate_pudding.jpg"),
]

# Crear pestañas
create_tab_items(foods_tab, food_items)
create_tab_items(drinks_tab, drink_items)
create_tab_items(desserts_tab, dessert_items)

# Resumen del pedido
summary_frame = tk.Frame(root)
summary_frame.pack(fill="x", pady=10)

tk.Label(summary_frame, text="Order Summary", font=("Arial", 14)).pack()

order_listbox = tk.Listbox(summary_frame, height=10)
order_listbox.pack(fill="both", padx=10, pady=5)

total_label = tk.Label(summary_frame, text="Total: ", font=("Arial", 12))
total_label.pack(side="left", padx=10)

total_value = tk.Label(summary_frame, textvariable=total_var, font=("Arial", 12))
total_value.pack(side="left")

order_button = tk.Button(summary_frame, text="Order", command=lambda: print("Order Placed!"))
order_button.pack(side="right", padx=10)

# Inicia la aplicación
root.mainloop()
