#!/bin/bash
# Setup script for Linux and macOS users

echo "Setting up Student Feedback System..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Prompt user to configure .env file
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    
    # Generate secret key
    echo "Generating SECRET_KEY..."
    python3 generate_secret_key.py
    
    echo ""
    echo "IMPORTANT: Edit the .env file and update the SECRET_KEY with the one generated above."
    echo ""
    read -p "Press Enter to continue..."
fi

# Initialize the project
echo "Initializing the project..."
python3 init_project.py

echo ""
echo "Setup complete! Run 'python3 manage.py runserver' to start the development server."
echo "Access the application at http://127.0.0.1:8000/"
echo ""
