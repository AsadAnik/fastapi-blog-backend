build:
	docker-compose build

build-no-cache:
	docker-compose build --no-cache

up:
	docker-compose up -d

up-dev:
	docker-compose up

up-build:
	docker-compose up --build

up-pg:
	docker-compose up --build postgres -d

up-pg-dev:
	docker-compose up --build postgres

pg-shell:
	docker-compose exec postgres psql -U postgres

down:
	docker-compose down

# Run Migrations
run-migration:
	alembic init alembic

# Create Migrations
create-migration:
	alembic revision --autogenerate -m "Initial migration"

# Apply Migrations
apply-migration:
	alembic upgrade head