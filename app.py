from flask import Flask, render_template, request, redirect, url_for, flash
from models import Inventario
from forms import ProductForm   # importar tu formulario

app = Flask(__name__)   # <---- AQUÍ defines app primero
app.secret_key = "supermercado2025"  # Necesario para Flask-WTF y mensajes flash

# Inicializamos inventario (BD SQLite)
inv = Inventario()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def list_products():
    productos = inv.mostrar_productos()
    return render_template("products/list.html", productos=productos)

@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        cantidad = form.cantidad.data
        precio = form.precio.data
        try:
            inv.agregar_producto(nombre, cantidad, precio)
            flash("✅ Producto agregado con éxito", "success")
            return redirect(url_for("list_products"))
        except Exception as e:
            flash(f"❌ Error: {e}", "danger")
    return render_template("products/form.html", form=form)

@app.route("/products/delete/<int:id_producto>")
def delete_product(id_producto):
    inv.eliminar_producto(id_producto)
    flash("🗑 Producto eliminado", "warning")
    return redirect(url_for("list_products"))

if __name__ == "__main__":
    app.run(debug=True)
