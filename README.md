# FastAPI Blog Project

This project is a **FastAPI**-based blogging platform. It utilizes **PostgreSQL** as the database and **Docker** for containerization. The project is designed to provide a lightweight, efficient, and scalable blog application with essential features like user authentication, post creation, and management.

## Table of Contents

- [Project Features](#project-features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Running the Project](#running-the-project)
- [Database Migrations](#database-migrations)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Development](#development)
- [Testing](#testing)
- [License](#license)

## Project Features

- **User Authentication**: Secure user registration and login.
- **Post Creation and Management**: CRUD operations for blog posts.
- **PostgreSQL Database**: Storing user data, posts, and other information.
- **Dockerized**: Easy setup and deployment with Docker.
- **API Documentation**: Auto-generated Swagger UI for easy interaction with the API.

## Technologies Used

- **FastAPI**: Backend framework for building APIs.
- **PostgreSQL**: Relational database for storing data.
- **Docker**: Containerization of the app and PostgreSQL.
- **Alembic**: Database migration tool for handling schema changes.
- **SQLAlchemy**: ORM (Object Relational Mapper) for working with the PostgreSQL database.

## Installation and Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** and **Docker Compose**: [Install Docker](https://docs.docker.com/get-docker/)
- **Python 3.8+**: [Install Python](https://www.python.org/downloads/)
- **Git**: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Running the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/fastapi-blog.git
    cd fastapi-blog
    ```

2. **Set up the environment variables**:

   Create a `.env` file in the root directory (use the `.env.example` file as a template).

   ```bash
   cp .env.example .env
   ```

   Edit the `.env` file with the necessary configurations for your PostgreSQL database.

3. **Run the application with Docker**:
    ```bash
    docker-compose up --build
    ```

   This will build and start the FastAPI application and PostgreSQL database in separate containers.

4. **Access the API**:

   The API will be available at: `http://localhost:8000`

   The interactive API documentation is available at: `http://localhost:8000/docs`

5. **Access the database**:
   
   You can connect to the PostgreSQL database using a tool like `psql` or `pgAdmin`:
   - Host: `localhost`
   - Port: `5432`
   - User: As specified in the `.env` file
   - Password: As specified in the `.env` file

## Database Migrations

To handle database migrations, this project uses **Alembic**. To run migrations:

1. **Create a new migration**:
   ```bash
   docker-compose exec fastapi_blog_app alembic revision --autogenerate -m "message"
   ```

2. **Apply migrations**:
   ```bash
   docker-compose exec fastapi_blog_app alembic upgrade head
   ```

## API Endpoints

- **`/auth/register`**: Register a new user.
- **`/auth/login`**: Log in a user.
- **`/posts`**: Create, read, update, and delete blog posts.
  
Full API documentation is available via **Swagger UI** at `http://localhost:8000/docs`.

## Environment Variables

The project relies on several environment variables to function correctly. These should be added to the `.env` file:

```bash
# Database configuration
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# FastAPI secret key for authentication
SECRET_KEY=your_secret_key
```

## Development

To run the project in development mode with hot-reloading:

1. Run the project:
   ```bash
   docker-compose up --build
   ```

2. The application will restart automatically on any code changes.

## Testing

To run tests, first, make sure the app is running:

```bash
docker-compose up
```

Then, you can run tests using `pytest`:

```bash
docker-compose exec fastapi_blog_app pytest
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---