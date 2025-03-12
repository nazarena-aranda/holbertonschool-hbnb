# 📌 HBnB - Proyecto

## 📖 Descripción del Proyecto

Este proyecto es una implementación de **HBnB**, una aplicación web que simula una versión muy simple de **Airbnb**. En esta fase, nos enfocamos en la construcción de una **API RESTful con Flask**, permitiendo a los usuarios:

✅ **Crear y actualizar usuarios**  
✅ **Publicar y actualizar lugares**  
✅ **Dejar reseñas sobre los lugares**  
✅ **Asociar amenities a los lugares**  



---

## 🏗️ Estructura del Proyecto

📂 **`hbnb/`** → Carpeta raíz del proyecto.   
📂 **`api/`** → Contiene los endpoints de la API.  
&nbsp;&nbsp;&nbsp;&nbsp;📂 **`v1/`** → Implementación de los endpoints  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📜 **`users.py`** → Manejo de usuarios: registro y obtención de datos del usuario  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📜 **`places.py`** → Administración de lugares: creació, listado y datos de los lugares.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📜 **`reviews.py`** → Gestión de reseñas: añadir, eliminar y mostrar los datos de las reseñas.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📜 **`amenities.py`** → Manejo de amenities: agregar y listar amenities.

📂 **`models/`** → Contiene la lógica de negocio y las clases de los endpoints.  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`base_model.py`** → Clase base con atributos compartidos (`id`, `created_at`, `updated_at`).  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`user.py`** → Modelo de usuario.  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`place.py`** → Modelo de lugar.  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`review.py`** → Modelo de reseñas.  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`amenity.py`** → Modelo de amenities.  

📂 **`persistencia/`** → Guarda los datos.  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`repositorio.py`** → Define el modelo de repositorio, aquí gestiona y almacena datos, como los usuarios, lugares y reseñas. 

📂 **`servicios/`** → Implementa el patrón **Facade** para simplificar la lógica del sistema.  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`facade.py`** → Centraliza la gestión de usuarios, lugares y reseñas.  

📜 **`run.py`** → Archivo principal para ejecutar la aplicación Flask.  
📜 **`config.py`** → Configuración de variables de entorno y ajustes generales.  
📜 **`requirements.txt`** → Lista de dependencias del proyecto, si no tenemos esto, nuestro servidor no va a correr.  

---

## 🏛️ Modelo de Datos

### 📌 **Clase `User`**
**Atributos:**
- `id`: Identificador único (UUID).
- `first_name`: Nombre del usuario.
- `last_name`: Apellido del usuario.
- `email`: Dirección de correo electronico.

### 📌 **Clase `Place`**
**Atributos:**
- `id`: Identificador único (UUID).
- `title`: Nombre del lugar.
- `description`: Descripción.
- `price`: Precio.
- `latitude`: Latitud del lugar.
- `longitude`: Longitud del lugar.
- `owner_id`: id del usuario propietario.

**Relaciones:**
- Un **usuario** puede ser dueño de varios **lugares**).
- Un **lugar** puede tener varias **reseñas**).
- Un **lugar** puede tener muchos **amenities**).

### 📌 **Clase `Review`**
**Atributos:**
- `id`: Identificador único (UUID).
- `text`: Contenido de la reseña.
- `rating`: Puntuación del lugar (1 a 5).
- `place_id`: Lugar al que pertenece la reseña.
- `user_id`: Usuario que escribió la reseña.

### 📌 **Clase `Amenity`**
**Atributos:**
- `id`: Identificador único (UUID).
- `name`: Nombre del servicio (ej. "WiFi", "Piscina").

---

## 🚀 Instalación y Ejecución

### 1️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2️⃣ Ejecutar la aplicación
```bash
python run.py
```

Esto levantará el servidor de Flask y asi la API permitirá interacción, puede ser tanto desde la url como usando Curl.

## 📌 **Autores**
- 💻 **Nazarena Aranda** - [GitHub](https://github.com/nazarena-aranda/nazarena-aranda)
- 💻 **Ignacio Devita** - [GitHub](https://github.com/nyacho04?tab=repositories&q=&type=&language=&sort=)
