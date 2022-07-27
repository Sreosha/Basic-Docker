# Basic-Docker using continuumio/anaconda3

Built and run docker and shown the output with the help of Flasgger and Flask api
To build the docker use the following command
  docker build -t <docker_container_name> .
To run the docker use the following command (used port 5000)
  docker run -d -p 5000:5000 <docker_container_name>
To check the output use the link ( used localhost )
  http://localhost:5000/apidocs
Upload a .png file present in repo and check the output.
