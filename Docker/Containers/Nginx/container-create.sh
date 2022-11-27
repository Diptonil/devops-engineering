# Used to start a container with the name 'Nginx', mapped to port 8080 on the local machine, in detached mode. The environment variable is being passed down for utilization (but here it is not really required and is just exemplary).

docker container run --name Nginx -p 8080:80 -d -e ENVIRONMENT_VARIABLE=value nginx