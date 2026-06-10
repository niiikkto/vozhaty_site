.PHONY: setup run check format docker-up docker-down logs clean

setup:
	@echo "🔧 Setting up local environment..."
	python -m venv venv
	.\venv\Scripts\activate && pip install --upgrade pip && pip install -r requirements.txt && pip install ruff black
	@echo "✅ Setup complete. Activate venv manually: .\\venv\\Scripts\\activate"

run:
	@echo "🚀 Running project locally..."
	python manage.py runserver

check:
	@echo "🔍 Running linter and checks..."
	ruff check .

format:
	@echo "🎨 Formatting code..."
	black .

docker-up:
	@echo "🐳 Starting containers..."
	docker compose up --build

docker-down:
	@echo "🛑 Stopping containers..."
	docker compose down

logs:
	@echo "📜 Showing logs..."
	docker compose logs -f

clean:
	@echo "🧹 Cleaning temporary files..."
	rm -rf __pycache__
	rm -rf */__pycache__
	@echo "Done."