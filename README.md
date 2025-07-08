# 🛡️ Spam Detector API using FastAPI and Ollama (Llama3.1:8b)

This project is a simple **Spam Message Detection API** powered by **FastAPI** and **Ollama** running the **Llama 3.1 8B** model locally.

---

## 🚀 Features
- Detects if a given message is **Spam** or **Not Spam**
- Uses **Llama 3.1 8B** running locally via **Ollama**
- Lightweight and easy to run anywhere

---

## 🧩 Tech Stack
- Python 3.8+
- FastAPI
- Uvicorn
- Requests
- Ollama (`llama3.1:8b` model)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>
```


### 2. Install Python Requirements
```  
pip install -r requirements.txt
  ```

### 3. Install Ollama (Run Local AI Models)
#### 👉 For Linux & Mac:
```
curl https://ollama.com/install.sh | sh
```

#### 👉 For Windows:
#### Download the installer from: 

https://ollama.com/download

### 4. Pull the Llama3.1 8B Model

```
ollama pull llama3.1:8b
```

#### Run llama
```
ollama run llama3.1:8b
```

### 5. Run the FastAPI App
```
uvicorn main:app --reload --port 8000
```

### You can test it with curl as well
```
curl -X POST "http://127.0.0.1:8000/check-spam/" \
-H "Content-Type: application/json" \
-d '{"content": "Congratulations! You have won $1000 cash prize. Click the link to claim."}'
```


