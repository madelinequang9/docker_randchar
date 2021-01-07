# docker_randchar
Used to Docker to deploy a web app that outputs 100 random characters that was previously written to a text file, and output 100 new random characters that will be written to the text file to replace previous characters.

This is the commands to create volumes:
1. Creating the volume: docker volume create [volume_name]   ex. docker volume create servervol
2. Mounting the volume: docker run -it --mount source=[volumename], destination=[destination_of_containter] [containter_image]
  ex. docker run -it --mount source=servervol,destination=/serverdata debian

To make a python file write: 
nano [pythonfile_name].py    ex. nano app/text_gen.py   

To get into the container shell, type:
docker exec -it [containter_name] /bin/bash (type docker ps to find the name of the containter)
In it, you can type and execute your commands. 

To build image:
docker build -t [image_name] .

To run the docker do and view the output contents:

docker run -d -p 5000:5000 [name_of_image]  ex. docker run -d -p 5000:5000 [assignment2]
curl [web-address]                          ex. curl http://localhost:5000

