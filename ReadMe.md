### Docker basic commands

`docker run <image name>` - runs a container. Image will be downloaded from docker registry if not present on the machine
`docker ps` - lists all running containers
`docker ps -a` - lists all containers (running or not running)
`docker stop <container name or id>` - stops running containers
`docker rm <continaer name or id>` - removes container
`docker images` - lists all images
`docker rmi <image name>` - remove downloaded image
`docker pull <image name>` - pulls the image from registry, but does not start the container
`docker exec <container name> <command>` - runs a command on running container

Containers are meant to run a specific task or process. Once the task is complete, the container exits.
Docker container only lives for the duration of the task running inside it. 
