Simple Api

The "Quotes API" project is a simple RESTful API built with FastAPI and SQLAlchemy. It provides endpoints to manage quotes, including creating new quotes and retrieving random quotes. The API is designed to be easy to use and can be integrated into various applications that require inspirational or random quotes.

	Key Features
Random Quote: Provides an endpoint to fetch a random quote from the database.

CRUD Operations: Implements basic CRUD operations for managing quotes in the database.

FastAPI: Utilizes the FastAPI framework for building the API endpoints.

SQLite Database: Uses SQLite as the database to store and retrieve quotes.

Postman Integration: Supports CRUD operations through Postman


	Project Structure:
models.py: Contains SQLAlchemy models for database interactions.

schemas.py: Defines Pydantic schemas for data validation.

database.py: Includes functions for database setup and connection.

main.py: FastAPI application file with API endpoints.

README.md: Documentation on project setup and API usage.

	Technologies Used:
FastAPI: Python framework for building APIs.

SQLAlchemy: ORM library for database interactions.

Pydantic: Data validation library for defining schemas.

SQLite: Lightweight SQL database engine.

Postman: Used for testing CRUD operations.
