format_w1s1:
	black *.py
	isort *.py

pycache:
	find ./ -type d -name '__pycache__' -exec rm -rf {} +