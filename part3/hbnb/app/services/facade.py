from app.persistence.repository import UserRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository

class HBnBFacade:
    def __init__(self):
        self.user_repository = UserRepository()
        self.place_repository = SQLAlchemyRepository(Place)
        self.review_repository = SQLAlchemyRepository(Review)
        self.amenity_repository = SQLAlchemyRepository(Amenity)

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repository.add(user)
        return user

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)

    def get_all_users(self):
        return self.user_repository.get_all()

    def create_place(self, place_data):
        owner = self.get_user_by_id(place_data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")

        amenities = []
        for amenity_id in place_data['amenities']:
            amenity = self.get_amenity(amenity_id)
            if not amenity:
                raise ValueError(f"Amenity {amenity_id} not found")

            amenities.append(amenity)

        place = Place(
            title=place_data['title'],
            description=place_data.get('description', ''),
            price=place_data['price'],
            latitude=place_data['latitude'],
            longitude=place_data['longitude'],
            owner=owner,
            amenities=amenities)
        self.place_repository.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def get_all_places(self):
        return self.place_repository.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
        for key, value in place_data.items():
            setattr(place, key, value)
        self.place_repository.update(place_id, place_data)
        return place

    def create_amenity(self, amenity_data):
        amenity = Amenity(amenity_data["name"])
        self.amenity_repository.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repository.get(amenity_id)
        if not amenity:
            raise ValueError("Amenity not found")
        return amenity

    def get_all_amenities(self):
        return self.amenity_repository.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            raise ValueError("Amenity not found")

        self.amenity_repository.update(
            amenity_id,
            {
                'name': amenity_data["name"]
            }
        )

    def create_review(self, review_data):
        place = self.get_place(review_data['place_id'])
        if not place:
            raise ValueError("Place not found")

        user = self.get_user_by_id(review_data['user_id'])
        if not user:
            raise ValueError("User not found")

        review = Review(**review_data)

        reviews = place.reviews
        reviews.append(review)

        self.place_repository.update(place.id, {
            'reviews': reviews
        })

        return review

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def get_all_reviews(self):
        return self.review_repository.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
        return place.reviews

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if not review:
            raise ValueError("Review not found")

        self.review_repository.update(review_id, {
            'text': review_data["text"],
            'rating': review_data["rating"]
        })

    def delete_review(self, review_id):
        self.review_repository.delete(review_id)