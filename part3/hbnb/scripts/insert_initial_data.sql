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
