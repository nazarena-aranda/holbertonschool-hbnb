import uuid
from datetime import datetime

class BaseModel:
    """Clase base con atributos comunes para las entidades"""
    
    def __init__(self):
        """Inicializa el objeto con un UUID y timestamps"""
        self.id = str(uuid.uuid4())  # Genera un UUID único
        self.created_at = datetime.now()  # Timestamp de creación
        self.updated_at = datetime.now()  # Última modificación

    def save(self):
        """Actualiza el timestamp de 'updated_at' cuando se modifica el objeto"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Permite actualizar atributos del objeto con un diccionario de datos"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Actualiza `updated_at` después de modificar los datos
