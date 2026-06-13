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