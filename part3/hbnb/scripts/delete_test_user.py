#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from app.services import facade

def delete_test_user():
    app = create_app()
    with app.app_context():
        test_user = facade.get_user_by_email('test@example.com')
        if test_user:
            facade.user_repository.delete(test_user)
            print("Usuario test@example.com eliminado exitosamente")
        else:
            print("El usuario test@example.com no existe")

if __name__ == '__main__':
    delete_test_user() 