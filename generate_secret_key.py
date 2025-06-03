#!/usr/bin/env python
"""
Generate a secure Django SECRET_KEY
Run this script to create a new secret key for your Django project
"""

import secrets
import string

def generate_secret_key(length=50):
    """Generate a secure random string for Django's SECRET_KEY setting"""
    chars = string.ascii_letters + string.digits + string.punctuation
    # Filter out characters that might cause issues in .env files
    chars = chars.replace("'", "").replace('"', '').replace('\\', '')
    
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("\nGenerated SECRET_KEY:")
    print(secret_key)
    print("\nAdd this to your .env file:")
    print(f"SECRET_KEY={secret_key}")
    print("\nRemember to keep this key secret and never commit it to version control!")
