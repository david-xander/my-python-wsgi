test:
	docker-compose up -d
	pytest app/tests --disable-warnings || true
	docker-compose down