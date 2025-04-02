from app.models.place import Place

def get_place(self, place_id):
    """Get a place by ID"""
    try:
        place = Place.query.get(place_id)
        if place is None:
            raise ValueError(f"No place found with ID: {place_id}")
        return place
    except Exception as e:

        print(f"Error retrieving place: {e}")
        return None