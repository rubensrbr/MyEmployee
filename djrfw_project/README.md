1. Clone the repository: git clone <https://github.com/rubensrbr/MyEmployee>
2. Navigate to the project directory: cd MyEmployee
3. Install uv: pip install uv
4. Sync uv with pyproject.toml: uv sync
5. Activate the virtual environment: uv activate
6. Build the Docker image for the database: docker-compose build
7. Start the Docker container for the database: docker-compose up -d
8. Apply the database dump: docker exec -i docker-db-1 psql -U postgres my_employee_db < dump.sql

Running the Application

1. Run the Django migrations:uv run python manage.py migrate
2. Start the Django development server:uv run python manage.py runserver
3. Access the application in your web browser: <http://localhost:8000>

No License
