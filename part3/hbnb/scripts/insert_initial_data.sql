-- user admin and password encrypt
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1', 
    'Admin', 
    'HBnB', 
    'admin@hbnb.io', 
    '$2b$12$9k1mNOT57qYDcieHAxELt.bU/1/a2il50VSl6975XIark4v96N8nW', -- bcrypt hash de 'admin1234'
    TRUE
);

-- initiales amenities
INSERT INTO amenities (id, name) VALUES 
    (uuid(), 'WiFi'),
    (uuid(), 'Swimming Pool'),
    (uuid(), 'Air Conditioning');


-- initiales places
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id) VALUES
    (uuid(), 'Casa en la playa', 'Descripción de la casa en la playa', 100.0, 33.4565, -112.0679, '36c9050e-ddd3-4c3b-9731-9f487208bbc1'),
    (uuid(), 'Apartamento en la ciudad', 'skibidi dop dop yes yes', 50.0, 40.7128, -74.0060, '36c9050e-ddd3-4c3b-9731-9f487208bbc1'),
    (uuid(), 'Hotel en la montaña', 'Descripción del hotel en la montaña', 150.0, 37.7749, -122.4194, '36c9050e-ddd3-4c3b-9731-9f487208bbc1'),
    (uuid(), 'Villa en el campo', 'Descripción de la villa en el campo', 200.0, 41.8902, 12.4523, '36c9050e-ddd3-4c3b-9731-9f487208bbc1');




