# HBnB - Airbnb Clone

A full-stack web application that replicates Airbnb functionalities, built with Flask.

## 🌟 Features

- **User Authentication & Authorization**
  - JWT-based authentication
  - Secure password hashing
  - Protected routes
  - User roles (admin/regular)

- **Property Management**
  - Create and list properties
  - Detailed property information
  - Location with coordinates
  - Price management
  - Property reviews and ratings

- **Review System**
  - Star ratings
  - Text reviews
  - User verification for reviews

- **Amenities**
  - Multiple amenities per property
  - Customizable amenity list
  - Search by amenities

## 🛠️ Technologies Used

- **Backend**
  - Flask (framework)
  - SQLAlchemy
  - Flask-RESTx (API documentation)
  - CORS

- **Frontend**
  - HTML
  - CSS
  - JavaScript (Vanilla)

- **Database**
  - SQLite

## 📝 API Endpoints

### Authentication
- `POST /api/v1/auth/signup` - Register new user
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/protected` - Protected route example

### Users
- `GET /api/v1/users` - List all users
- `POST /api/v1/users` - Create user
- `GET /api/v1/users/<id>` - Get user details
- `PUT /api/v1/users/<id>` - Update user
- `DELETE /api/v1/users/<id>` - Delete user

### Places
- `GET /api/v1/places` - List all places
- `POST /api/v1/places` - Create place
- `GET /api/v1/places/<id>` - Get place details
- `PUT /api/v1/places/<id>` - Update place
- `DELETE /api/v1/places/<id>` - Delete place

### Reviews
- `GET /api/v1/reviews` - List all reviews
- `POST /api/v1/reviews` - Create review
- `GET /api/v1/reviews/<id>` - Get review details

### rerequisites
- Python 3+
- pip

### Installation

1. **Set up Python virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   cd part3/hbnb
   pip install -r requirements.txt
   ```

3. **Start the Flask server**
   ```bash
   python -m flask run
   ```

4. **Start the frontend server**
   ```bash
   cd ../../part4/base_files
   python -m http.server 8000
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`
   - API documentation available at `http://localhost:5000`

### Test User Credentials
- Email: `test@example.com`
- Password: `password123`

## 📝 Data Models

### User
```python
{
    "id": "uuid",
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "is_admin": "boolean"
}
```

### Place
```python
{
    "id": "uuid",
    "title": "string",
    "description": "string",
    "price": "float",
    "latitude": "float",
    "longitude": "float",
    "user_id": "uuid"
}
```

### Review
```python
{
    "id": "uuid",
    "text": "string",
    "rating": "integer(1-5)",
    "place_id": "uuid",
    "user_id": "uuid"
}
```

## Technical Documentation of the project:
https://docs.google.com/document/d/1XmEArb75nL2b73Zwn-jP_XrlNaX99pQgfMupUj2m_Yc/edit?tab=t.0#heading=h.r5at5axqla1d

## 👥 Authors

- [Ignacio Devita](https://github.com/nyacho04)
- [Nazarena Aranda](https://github.com/nazarena-aranda)
