# Student Feedback System

A complete Django-based web application for collecting and managing student feedback for educational courses. This system allows students to submit feedback and instructors/administrators to review, filter, and manage the feedback.

![Student Feedback System](static/feedback/img/screenshot.png)

## Features

- **Student Portal**: Simple form for students to submit course feedback with ratings
- **Admin Dashboard**: Secure interface for administrators to review all feedback
- **Filtering System**: Filter feedback by course, status, or other criteria
- **Authentication**: Secure login for administrative users
- **Responsive Design**: Works on desktop and mobile devices
- **Data Visualization**: Visual representation of feedback metrics

## Tech Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default), easily configurable for PostgreSQL, MySQL, etc.
- **Authentication**: Django's built-in authentication system
- **Security**: CSRF protection, XSS prevention, secure cookies

## Installation Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setup Instructions (All Operating Systems)

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/student-feedback-system.git
cd student-feedback-system
```

#### 2. Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables

Create a `.env` file in the student_feedback directory with the following variables:

```
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

For production deployment, set `DEBUG=False` and add your domain to `ALLOWED_HOSTS`.

#### 5. Initialize the Project

This will set up the database, create a superuser, and add sample data:

**On Windows:**
```bash
cd student_feedback
python init_project.py
```

**On macOS/Linux:**
```bash
cd student_feedback
python3 init_project.py
```

#### 6. Run the Development Server

**On Windows:**
```bash
python manage.py runserver
```

**On macOS/Linux:**
```bash
python3 manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the application.

### Default Admin Credentials

- **Username**: admin
- **Password**: adminpassword

**Important**: Change these credentials immediately for any production use!

## Usage Guide

### For Students:
1. Visit the homepage
2. Fill out the feedback form with your name, course, rating, and comments
3. Submit the form

### For Administrators:
1. Visit /admin-login/
2. Log in with your admin credentials
3. View all feedback in the dashboard
4. Filter feedback by course or status
5. Mark feedback as addressed or delete it as needed

## Customization

### Changing the Database

To use a different database (e.g., PostgreSQL), update the `DATABASES` configuration in `settings.py` and set the appropriate environment variables.

### Adding New Features

The modular structure makes it easy to add new features:
1. Add new models in `models.py`
2. Create corresponding views in `views.py`
3. Update templates in the `templates` directory
4. Add URL routes in `urls.py`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions or feedback, please open an issue on GitHub or contact [your-email@example.com].
