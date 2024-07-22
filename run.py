"""This is the file that will be executed to run the Flask application.
run python run.py in the terminal to start the application."""
from app.app import app

if __name__ == "__main__":
    app.run(debug=True)
