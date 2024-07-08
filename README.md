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

**2. Create an S3 Bucket**
* Go to the S3 console in AWS.
* Create a new bucket and name it ***t2s-form-submissions***. 

**3. Create a DynamoDB Table**
* Go to the DynamoDB console in AWS.
* Create a new table and name it ***T2SFormSubmissions***.
* Primary Key should be ***submission_id** (String).

**4. Create a Lambda Function**
* Create a Lambda function that will handle the submissions for the form and name it ***lambda-function.py***.

**5. Set Up API Gateway**
* Go to the API Gateway console in AWS.
* Create a new REST API.
* Create a new resource (e.g., /submit_form).
* Create a new POST method for the resource.
* Integrate the POST method with the Lambda function created earlier.
* Deploy the API to a new stage (e.g., prod).

**6. Create S3 Bucket, DynamoDB, CloudWatch Logs, and Trust Policies**
* Create policies.
* Create an IAM Role for Lambda service. 

**6. Move into the working directory:**
* cd docker-webform

**7. Modify the HTML Form to Submit to the API**
* Update the form action URL in the HTML to point to the API Gateway endpoint by replacing the ***<api-id>*** with your ***API Gateway ID***. 

**8. Build and Run Docker Compose:**
* docker-compose build
* docker-compose up

**9. Validate:**
* Open your browser and go to http://localhost:8080🌐.
* If you did not change the code, you should see your website live with this message: "Hello, World, from Dr. Emmanuel here at T2S!"

**10. Clean Up:**
* docker-compose down

## Troubleshooting:
* 🚨 Make sure Docker is running and you have sufficient resources allocated.
* 🛠️ Check container logs using docker logs <container_name> if something goes wrong. Use this command, "docker-compose logs myapp." Replace 'myapp' with the name of your application. 


## Outro:
* 🎉 Congrats! You have successfully deployed a website built on a node.js script and using Docker Compose.
* 💬 Leave any questions or comments below; I'll gladly help!
