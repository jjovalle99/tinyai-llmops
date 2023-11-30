format:
	black *.py
	isort *.py

pycache:
	find ./ -type d -name '__pycache__' -exec rm -rf {} +
