End-to-end-ML-Project

Workflows:

1. exception,logger and utils(custom functions)
2. data ingestion
3. data transformation
4. model training
5. Update Predict Pipeline
6. Update the app.py

How to run?

Steps: 
conda create --p venv python==3.8 -y

conda activate venv/

pip install -r requirements.txt

python app.py

now run your local host 0.0.0.0:8080


AWS-CICD-Deployment-with-Github-Actions

1. Login to AWS console.

2. Create IAM user for deployment

#with specific access

 EC2 access : It is virtual machine

 ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

 Build docker image of the source code

 Push your docker image to ECR

 Launch Your EC2 

 Pull Your image from ECR in EC2

 Lauch your docker image in EC2

#Policy:

 AmazonEC2ContainerRegistryFullAccess

 AmazonEC2FullAccess


3. Create ECR repo to store/save docker image

- Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject

4. Create EC2 machine (Ubuntu)

5. Open EC2 and Install docker in EC2 Machine:

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

6. Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one


7. Setup github secrets:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app