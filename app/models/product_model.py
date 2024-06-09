from app.database import db


# Define la clase `Product` que hereda de `db.Model`
# `Product` representa la tabla `Products` en la base de datos
class Product(db.Model):
    __tablename__ = "products"

    # Define las columnas de la tabla `Products`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    # Inicializa la clase `Product`
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    # Guarda un Product en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los Productes de la base de datos
    @staticmethod
    def get_all():
        return Product.query.all()

    # Obtiene un Product por su ID
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)

    # Actualiza un Product en la base de datos
    def update(self, name=None, description=None, price=None, stock=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if stock is not None:
            self.stock = stock
        db.session.commit()

    # Elimina un Product de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()