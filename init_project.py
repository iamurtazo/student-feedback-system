#!/usr/bin/env python
"""
Initialization script for Student Feedback System
This script will:
1. Run migrations to set up the database
2. Create a superuser for admin access
"""

import os
import django
import sys

# Set up Django
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_feedback.settings')
django.setup()

# Now we can import Django models
from django.contrib.auth.models import User
from feedback.models import Feedback
from django.db import transaction

def run_migrations():
    """Run database migrations"""
    print("Running migrations...")
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')

def create_superuser():
    """Create a superuser for admin access if one doesn't exist"""
    if not User.objects.filter(is_superuser=True).exists():
        print("Creating superuser...")
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )
        print("Superuser created with username 'admin' and password 'adminpassword'")
    else:
        print("Superuser already exists")

def create_sample_data():
    """Create some sample feedback data"""
    if Feedback.objects.count() == 0:
        print("Creating sample feedback data...")
        
        sample_data = [
            {
                'name': 'John Smith',
                'course': 'Introduction to Python',
                'rating': 5,
                'comment': 'Excellent course! The instructor explained complex concepts in a very understandable way.',
                'status': 'pending'
            },
            {
                'name': 'Sarah Johnson',
                'course': 'Web Development Bootcamp',
                'rating': 4,
                'comment': 'Great course with lots of practical examples. Could use more exercises though.',
                'status': 'pending'
            },
            {
                'name': 'Mike Brown',
                'course': 'Introduction to Python',
                'rating': 3,
                'comment': 'The course was okay, but moved too fast in some sections.',
                'status': 'addressed'
            },
            {
                'name': 'Emily Davis',
                'course': 'Database Design',
                'rating': 5,
                'comment': 'Very detailed explanations and plenty of practical assignments.',
                'status': 'pending'
            },
            {
                'name': 'Robert Wilson',
                'course': 'Machine Learning Basics',
                'rating': 2,
                'comment': 'Too advanced for beginners. Prerequisites should be clearly mentioned.',
                'status': 'pending'
            }
        ]
        
        with transaction.atomic():
            for data in sample_data:
                Feedback.objects.create(**data)
                
        print(f"Created {len(sample_data)} sample feedback entries")

if __name__ == '__main__':
    run_migrations()
    create_superuser()
    create_sample_data()
    print("\nInitialization complete! You can now run the server with 'python manage.py runserver'")
    print("Access the admin interface at http://127.0.0.1:8000/admin/ with username 'admin' and password 'adminpassword'")
    print("Access the main site at http://127.0.0.1:8000/")
