import unittest
from app import app
from app.models.user import User

class TestUserModel(unittest.TestCase):
    def test_valid_user(self):
        user = User(first_name="John", last_name="Doe", email="john@example.com")
        errors = user.validate()
        self.assertEqual(len(errors), 0)

    def test_invalid_email(self):
        user = User(first_name="John", last_name="Doe", email="invalid-email")
        errors = user.validate()
        self.assertIn("Invalid email format", errors)

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_user_valid(self):
        response = self.client.post('/api/v1/users', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid(self):
        response = self.client.post('/api/v1/users', json={
            "first_name": "",
            "last_name": "",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("errors", response.json)

if __name__ == '__main__':
    unittest.main()