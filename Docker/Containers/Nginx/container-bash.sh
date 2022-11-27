# To run an Nginx container on an interactive mode by overriding its default command. Instead, bash would run.

docker container run --name Nginx -p 8080:80 -d -it nginx bash