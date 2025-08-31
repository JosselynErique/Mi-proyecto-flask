from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class ProductForm(FlaskForm):
    nombre = StringField("Nombre", validators=[
        DataRequired(message="El nombre es obligatorio"),
        Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
    ])
    cantidad = IntegerField("Cantidad", validators=[
        DataRequired(message="La cantidad es obligatoria"),
        NumberRange(min=1, message="La cantidad debe ser mayor a 0")
    ])
    precio = DecimalField("Precio", validators=[
        DataRequired(message="El precio es obligatorio"),
        NumberRange(min=0.01, message="El precio debe ser mayor a 0")
    ])
    submit = SubmitField("Guardar")
