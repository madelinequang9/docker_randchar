# docker_randchar
This is the commands to create volumes:
1. Creating the volume: docker volume create [volume_name]   ex. docker volume create servervol
2. Mounting the volume: docker run -it --mount source=[volumename], destination=[destination_of_containter] [containter_image]
  ex. docker run -it --mount source=servervol,destination=/serverdata debian

To make a python file write: 
nano [pythonfile_name].py    ex. nano app/text_gen.py   

To get into the container shell, type:
docker exec -it [containter_name] /bin/bash (type docker ps to find the name of the containter)
In it, you can type and execute your commands. 
