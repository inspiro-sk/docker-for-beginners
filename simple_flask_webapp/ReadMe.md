### Simple Flask webapp

First build the container by running:
```
docker build -t <your tag> .
```

To run the container and map respective port on your machine to access Flask application port 8080 use the following command:
```
docker run -d -p 5000:8080 --name <your container name> <your tag>
```

Then you can access the application on `http://localjhost:5000`
