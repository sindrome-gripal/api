
install: 
	pip install -r requirements.txt	


run-dev:
	uvicorn main:app --reload --port 8080


deploy:
	git push heroku master


build-run:
	sudo docker build -t works-api . && \
	sudo docker run --restart=always --env-file=.env -p 8080:8080 works-api:latest 
