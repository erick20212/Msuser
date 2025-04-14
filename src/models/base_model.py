# src/models/base_model.py
class BaseModelMixin:
    def to_dict(self):
        """Devuelve un diccionario con los valores de las columnas del modelo."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        """Representación de cadena del objeto."""
        return f"<{self.__class__.__name__} {self.id}>"