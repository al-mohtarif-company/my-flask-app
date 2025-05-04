# This file contains configuration settings for the Flask application.
# The settings include database connection details, which are essential for
# connecting Flask to PostgreSQL via SQLAlchemy.

import os  # Standard library to interact with the operating system

# Database connection settings (you will need to replace these with your actual credentials)
DB_USER = "postgres"  # Database username (default is usually 'postgres')
DB_PASSWORD = "123456"  # Your PostgreSQL password
DB_NAME = "employee_evaluation"  # The name of the database you're using
DB_HOST = "localhost"  # Database host, typically 'localhost' for local development
DB_PORT = "5432"  # Default port used by PostgreSQL

# Constructing the SQLAlchemy database URI. This is a standard format for connecting to PostgreSQL
# The URI format is: postgresql://username:password@hostname:port/database_name
SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# This setting prevents SQLAlchemy from tracking modifications of objects for performance reasons
SQLALCHEMY_TRACK_MODIFICATIONS = False
