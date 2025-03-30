#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.services import facade

def init_db():
    app = create_app()
    with app.app_context():
        test_user = facade.get_user_by_email('test@example.com')
        if not test_user:
            facade.create_user({
                "first_name": "Test",
                "last_name": "User",
                "email": "test@example.com",
                "password": "password123",
                "is_admin": False
            })

if __name__ == '__main__':
    init_db() 