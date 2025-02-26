#Hbnb

The app/ directory contains the core application code.

The api/ subdirectory houses the API endpoints, organized by version (v1/).

The models/ subdirectory contains the business logic classes (e.g., user.py, place.py).

The services/ subdirectory is where the Facade pattern is implemented, managing the interaction between layers.

The persistence/ subdirectory is where the in-memory repository is implemented. This will later be replaced by a database-backed solution using SQL Alchemy.

run.py is the entry point for running the Flask application.

config.py will be used for configuring environment variables and application settings.

requirements.txt will list all the Python packages needed for the project.

README.md will contain a brief overview of the project.

BaseModel (Base Class)  it provide common attributes (id, created_at, updated_at) and basic methods (save, update) for all entities.

User - Represents a user in the system. a User can own multiple place instances.
Attributes:
first_name (String): User's first name (required, max 50 characters).
last_name (String): User's last name (required, max 50 characters).
email (String): User's email address (required, unique, valid format).
is_admin (Boolean): Indicates if the user has admin privileges.

Place - Represents a rental place. a place can have multiple Amenity and Review instances.
Attributes:
title (String): Title of the place (required, max 100 characters).
description (String): Detailed description of the place (optional).
price (Float): Price per night for the place (must be a positive value).
latitude (Float): Latitude of the place's location (range: -90.0 to 90.0).
longitude (Float): Longitude of the place's location (range: -180.0 to 180.0).
owner (User): User who owns the place.

Review - Represents a review written by a user about a place. a Review is associated with a Place and a User.
Attributes:
text (String): Content of the review (required).
rating (Integer): Rating for the place (range: 1 to 5).
place (Place): Place associated with the review.
user (User): User who wrote the review.

Amenity - Represents an amenity offered by a place. can be associated with multiple Place instances.
Attributes:
name (String): Name of the amenity (required, max 50 characters).