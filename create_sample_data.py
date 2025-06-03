#!/usr/bin/env python
"""
Script to populate the database with sample feedback entries
"""

import os
import django
import sys

# Set up Django environment
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_feedback.settings')
django.setup()

from feedback.models import Feedback
from django.db import transaction

def create_sample_data():
    """Create sample feedback entries"""
    print(f"Current feedback count: {Feedback.objects.count()}")
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
    else:
        print(f"Database already has {Feedback.objects.count()} feedback entries. No sample data created.")

if __name__ == '__main__':
    create_sample_data()
