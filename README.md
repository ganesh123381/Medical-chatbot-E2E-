# Medical-chatbot-E2E-

# How to run?

# STEPS:

# Clone the repository
'''bash
git clone https://github.com/ganesh123381/Medical-chatbot-E2E-.git
'''

## STEP 01- Create a conda environment after opening the repository
'''bash
conda create -n medibot python=3.10 -y
conda activate medibot
'''

## STEP 02- install the requirements
'''bash
pip install -r requirements.txt
'''

## Create a .env file in the root directory and add your Pinecone & openai credentials as follows:
'''bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
'''

# run the following command to store embeddings to pinecone
'''bash
python store_index.py
'''

# Finally run the following command
'''bash
python app.py
'''

Now,
'''bash
open up localhost:
'''

### Techstack Used:

-Python
-LangChain
-Flask
-llama
-Pinecone

# AWS-CICD-Deployment-with-Github-Actions

##  1.Login to AWS console.

## 2.Create IAM user for deployment
'''bash
  
   #with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
'''

## 3. Create ECR repo to store/save docker image

''bash
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
    '''
## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

'''bash
    #optional

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
'''

## 6. Configure EC2 as self-hosted runner:
'''bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
'''

## 7. Setup github secrets:
  
1) AWS_ACCESS_KEY_ID
2) AWS_SECRET_ACCESS_KEY
3) AWS_DEFAULT_REGION
4) ECR_REPO
5) PINECONE_API_KEY
6) GROQ_API_KEY