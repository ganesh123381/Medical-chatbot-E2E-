# Medical-chatbot-E2E-

## How to Run?

### STEPS:

### Clone the Repository

```bash
git clone https://github.com/your-username/Medical-chatbot-E2E-.git
```

### STEP 01 - Create a Conda Environment

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

### STEP 02 - Install Requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` File

Create a `.env` file in the root directory and add your Pinecone & Groq credentials:

```bash
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Store Embeddings in Pinecone

```bash
python store_index.py
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```bash
http://localhost:5000
```

---

## Tech Stack Used

- Python
- LangChain
- Flask
- Llama
- Pinecone

---

# AWS CI/CD Deployment with GitHub Actions

## 1. Login to AWS Console

---

## 2. Create IAM User for Deployment

### Required Access

1. EC2 Access (Virtual Machine)
2. ECR Access (Elastic Container Registry)

### Deployment Workflow

1. Build Docker image from source code
2. Push Docker image to Amazon ECR
3. Launch EC2 Instance
4. Pull Docker image from ECR in EC2
5. Launch Docker container in EC2

### IAM Policies

```text
AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
```

---

## 3. Create ECR Repository

Save the ECR URI:

```bash
315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
```

---

## 4. Create EC2 Machine (Ubuntu)

---

## 5. Install Docker on EC2

### Update Packages

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```

### Install Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

---

## 6. Configure EC2 as Self-Hosted Runner

```text
Settings → Actions → Runners → New Self Hosted Runner
```

Choose your OS and execute the commands provided by GitHub.

---

## 7. Setup GitHub Secrets

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
PINECONE_API_KEY
GROQ_API_KEY
```