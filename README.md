## Introduction:

* 👋 Hey everyone! Welcome back to my GitHub.
* 🎥 This repo shows you how to deploy a website using Docker Compose and a Node.js script for the deployment.
* 📊 HTML (HyperText Markup Language) is the standard markup language used to create and design web pages by defining their structure and content through various tags and elements.

## Prerequisites:
* 💻 A computer with Docker and Docker Compose installed.
* 📁 Basic understanding of Docker and command-line interface.

## Steps:
**1. Get the codes/scripts from this repo.**
* git clone https://github.com/Here2ServeU/docker-webform
* cd docker-webform

**2. Build and Run Docker Compose:**
* docker-compose build
* docker-compose up

**3. Validate:**
* Open your browser and go to http://localhost:8080🌐.
* If you did not change the code, you should have a submission form. However, the form doesn't input data into any storage service, so if you try to fill it out, you will get an error!
* I will be making a video about how you can connect this form to any storage service on AWS, or some other cloud platforms. 

**4. Clean Up:**
* docker-compose down

## Troubleshooting:
* 🚨 Make sure Docker is running and you have sufficient resources allocated.
* 🛠️ Check container logs using docker logs <container_name> if something goes wrong. Use this command, "docker-compose logs myapp." Replace 'myapp' with the name of your application. 


## Outro:
* 🎉 Congrats! You have successfully deployed a website built on an HTML script using Docker Compose.
* 💬 Leave any questions or comments below; I'll gladly help!
