#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.services import facade
from app.models.place import Place
from app.models.amenity import Amenity

def seed_places():
    app = create_app()
    with app.app_context():
        # Get or create test user
        test_user = facade.get_user_by_email('test@example.com')
        if not test_user:
            test_user = facade.create_user({
                "first_name": "Test",
                "last_name": "User",
                "email": "test@example.com",
                "password": "password123",
                "is_admin": False
            })

        # Create amenities
        amenities = [
            Amenity("WiFi"),
            Amenity("Pool"),
            Amenity("Kitchen"),
            Amenity("Air Conditioning"),
            Amenity("Parking"),
            Amenity("Beach Access"),
            Amenity("Mountain View"),
            Amenity("City View")
        ]
        for amenity in amenities:
            try:
                facade.amenity_repository.add(amenity)
            except:
                pass  # Amenity might already exist

        # Clear existing places
        existing_places = facade.get_all_places()
        for place in existing_places:
            facade.place_repository.delete(place)

        # New places
        places = [
            {
                "title": "Beautiful Beach House",
                "description": "Stunning beachfront property with panoramic ocean views. Perfect for family vacations or romantic getaways. Features a private pool and direct beach access.",
                "price": 250.0,
                "latitude": 25.7617,
                "longitude": -80.1918,
                "amenities": ["WiFi", "Pool", "Kitchen", "Air Conditioning", "Beach Access"]
            },
            {
                "title": "Cozy Cabin",
                "description": "Charming mountain cabin surrounded by nature. Enjoy peaceful evenings by the fireplace and breathtaking mountain views. Perfect for nature lovers.",
                "price": 180.0,
                "latitude": 39.7392,
                "longitude": -104.9903,
                "amenities": ["WiFi", "Kitchen", "Air Conditioning", "Mountain View"]
            },
            {
                "title": "Modern Apartment",
                "description": "Contemporary apartment in the heart of the city. Close to restaurants, shopping, and entertainment. Features modern amenities and stunning city views.",
                "price": 150.0,
                "latitude": 40.7128,
                "longitude": -74.0060,
                "amenities": ["WiFi", "Kitchen", "Air Conditioning", "Parking", "City View"]
            }
        ]

        # Create places
        for place_data in places:
            try:
                place = Place(
                    title=place_data["title"],
                    description=place_data["description"],
                    price=place_data["price"],
                    latitude=place_data["latitude"],
                    longitude=place_data["longitude"],
                    owner_id=test_user.id
                )
                
                # Add amenities
                for amenity_name in place_data["amenities"]:
                    amenity = next((a for a in amenities if a.name == amenity_name), None)
                    if amenity:
                        place.add_amenity(amenity)
                
                facade.place_repository.add(place)
                print(f"Created place: {place.title}")
            except Exception as e:
                print(f"Error creating place {place_data['title']}: {str(e)}")

if __name__ == '__main__':
    seed_places() 