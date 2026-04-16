# 🌟 Celebrity Detector & QA System - Spotlight Intelligence

An end-to-end AI-powered application that allows users to:

- 📸 Upload an image of a celebrity  
- 🤖 Detect which celebrity is present in the image  
- 💬 Ask questions about the detected celebrity  
- 🧠 Get intelligent answers using LLM (Llama-4 via Groq)

---

## 🚀 Features

- 🔍 Celebrity Detection using Computer Vision
- 🧠 LLM-powered Question Answering (Groq + Llama-4)
- 🌐 Flask-based Web Interface
- ⚡ Fast API Inference Pipeline
- 🐳 Dockerized Application
- ☁️ Kubernetes Deployment (GKE)
- 🔄 CI/CD using CircleCI
- 📊 Logging & Error Handling

---

## 🏗️ Project Structure

```
app/
│
├── common/
│   ├── custom_exception.py
│   ├── logger.py
│
├── config/
│
├── utils/
│   ├── celebrity_detector.py
│   ├── image_handler.py
│   ├── qa_engine.py
│
├── routes.py
│
templates/
│   └── index.html
│
├── app.py
├── Dockerfile
├── kubernetes-deployment.yaml
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Tech Stack

- **Backend:** Flask (Python)
- **Computer Vision:** OpenCV
- **LLM:** Llama-4 via Groq API
- **Deployment:** Docker + Kubernetes (GKE)
- **CI/CD:** CircleCI
- **Cloud:** Google Cloud Platform (GCP)

---

## 🔄 Workflow

1. User uploads an image via UI
2. Image is processed using OpenCV
3. Celebrity is detected using ML logic
4. Detected name is passed to LLM
5. User asks questions about the celebrity
6. LLM generates contextual answers

---

## 🧪 Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/Sumit-Prasad01/Spotlight-Intelligence.git
cd celebrity-detector
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```
python app.py
```

Visit:
```
http://localhost:5000
```

---

## 🐳 Docker Setup

### Build Image
```
docker build -t celebrity-detector .
```

### Run Container
```
docker run -p 5000:5000 celebrity-detector
```

---

## ☁️ Kubernetes Deployment (GKE)

```
kubectl apply -f kubernetes-deployment.yaml
```

---

## 🔄 CI/CD Pipeline (CircleCI)

- Automatic build & test
- Docker image push to GAR
- Deployment to GKE

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|---------|--------|------------|
| `/` | GET | POST | Home Page | Upload Image | Ask Questions |

---

## 📸 Example Use Case

1. Upload image of a celebrity (e.g., Elon Musk)
2. System detects: *Elon Musk*
3. Ask:  
   - "What is his net worth?"  
   - "Which companies does he own?"  
4. Get intelligent AI-generated answers

---

## ⚠️ Limitations

- Accuracy depends on image quality
- Limited to trained celebrity dataset
- LLM responses depend on API latency

---

## 🔮 Future Improvements

- Face Recognition using Deep Learning (FaceNet / ArcFace)
- Multi-face detection
- Voice-based queries
- Real-time video processing

---

