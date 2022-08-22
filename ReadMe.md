### Basic Docker commands
`docker run <image name>`  runs a container. Image will be downloaded from docker registry if not present on the machine

`docker ps` lists all running containers

`docker ps -a` lists all containers (running or not running)


`docker stop <container name or id>` stops running containers

`docker rm <container name or id>` removes container

`docker images` lists all images

`docker rmi <image name>` remove downloaded image

`docker pull <image name>` pulls the image from registry, but does not start the container

`docker run <image name> <command>`runs a command on running container

### Running a container

to run a container use `docker run <image name>` command. This runs the container in attached mode and you will see the results in coonsole (i.e. you will not be able to use the console anymore). Use `-d` option to run the container in detached mode.

Containers are meant to run a specific task or process. Once the task is complete, the container exits.
Docker container only lives for the duration of the task running inside it.


### Dockerfile example

```
FROM <base image>

RUN <command to run>

WORKDIR <set working directory on container>

COPY <what> <where>

# define basic command to be executed on containers
ENTRYPOINT <command>

# define additional commands to be passed in / after ENTRYPOINT command
CMD ["<command>", "<parameters>"]
```