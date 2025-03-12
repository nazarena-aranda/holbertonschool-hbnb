#  HBnB - Proyect

##  Description of the project

This project is an implementation of HBnB, a web application that emulates a very simple version of Airbnb. In this phase, we focused on building a RESTful API with Flask, allowing users to:

**Create and update users**  
**Publish and update places**  
**Leave reviews for places**  
**Associate services with places**  


---

## Project Structure

📂 **`hbnb/`** → Project root folder.   
📂 **`api/`** → Contains the API endpoints.
&nbsp;&nbsp;&nbsp;&nbsp;📂 **`v1/`** → Implementation of endpoints
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📜 **`users.py`** → User management: registration and obtaining user data  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📜 **`places.py`** → Place management: creation, listing, and data for places. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📜 **`reviews.py`** → Review Management: Add, delete, and display review data.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📜 **`amenities.py`** → Amenity management: add and list amenities.

📂 **`models/`** → Contains the business logic and endpoint classes.  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`base_model.py`** → Base class with shared attributes (`id`, `created_at`, `updated_at`).  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`user.py`** → User model
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`place.py`** → Place model  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`review.py`** → Review model  
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`amenity.py`** → amenities model  

📂 **`persistencia/`** → saves the data
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`repositorio.py`** → Defines the repository model, where you manage and store data such as users, locations, and reviews.

📂 **`servicios/`** → Implement the **Facade** to simplify the logic   
&nbsp;&nbsp;&nbsp;&nbsp;📜 **`facade.py`** → Centralizes the management of users, places and reviews.  

📜 **`run.py`** → Main file to run the Flask application.  
📜 **`config.py`** → Setting environment variables and general settings.
📜 **`requirements.txt`** → List of project dependencies.

---

## Data Model

### 📌 **Class `User`**
**Attributes:**
- `id`: Unique identifier (UUID).
- `first_name`: User's first name.
- `last_name`: User's last name.
- `email`: Email address.

### 📌 **Class `Place`**
**Attributes:**
- `id`: Unique identifier (UUID).
- `title`: Name of the place.
- `description`: Description.
- `price`: Price.
- `latitude`: Latitude of the place.
- `longitude`: Longitude of the place.
- `owner_id`: ID of the user who owns the place.

**Relationships:**
- A **user** can own multiple **places**).
- A **place** can have multiple **reviews**).
- A **place** can have multiple **amenities**).

### 📌 **Class `Review`**
**Attributes:**
- `id`: Unique identifier (UUID).
- `text`: Content of the review.
- `rating`: Place rating (1 to 5).
- `place_id`: Place the review belongs to.
- `user_id`: User who wrote the review.

### 📌 **Class `Amenity`**
**Attributes:**
- `id`: Unique identifier (UUID).
- `name`: Name of the service (e.g., "WiFi", "Pool").

---

## 🚀 Instalation and execution

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Execute the aplication
```bash
python run.py
```

This will launch the Flask server and the API will allow interaction.

## 📌 **Autores**
[Ignacio Devita](https://github.com/nyacho04)
[Nazarena Aranda](https://github.com/nazarena-aranda)
