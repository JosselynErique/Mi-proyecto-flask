from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return '¡Hola! Bienvenido a mi aplicación Flask.'

# Ruta dinámica con parámetro
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Bienvenido, {nombre}!'

# Nueva ruta estática
@app.route('/about')
def about():
    return 'Esta es una página de información de la aplicación.'

# Nueva ruta con número como parámetro
@app.route('/doble/<int:num>')
def doble(num):
    return f'El doble de {num} es {num * 2}.'

if __name__ == '__main__':
    app.run(debug=True)
