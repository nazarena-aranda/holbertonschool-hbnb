#  HBnB - Proyect

##  Description of the project

This project is an implementation of HBnB, a web application that emulates a very simple version of Airbnb. In this phase, we focused on building a RESTful API with Flask, allowing users to:

**Create and update users**  
**Publish and update places**  
**Leave reviews for places**  
**Associate services with places**  


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
