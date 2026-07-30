# 🐾 AI-Powered Wildlife Population Intelligence System

An enterprise-grade, multi-modal biodiversity monitoring platform that leverages Computer Vision, Bioacoustics, and Geospatial Analytics to monitor species, estimate populations, analyze habitat health, and generate automated conservation recommendations.

---

## 📌 Project Overview
Monitoring biodiversity at scale requires processing vast amounts of unstructured telemetry data (camera trap images, field audio, coordinates). This system provides a unified intelligence engine capable of:
* **Camera Trap Image Detection:** Automated bounding box detection and species identification using YOLOv8 & EfficientNet/ResNet50.
* **Bioacoustic Signal Processing:** Classification of avian and fauna vocalizations from continuous audio streams using Mel-Spectrogram CNNs.
* **Spatial & Geospatial Analytics:** Mapping species occurrences and population densities utilizing GBIF records and local sensor sites.
* **Role-Based Conservation Workflows:** Granular RBAC supporting Researchers, Conservation Officers, Forest Department Personnel, and System Administrators.

---

## 🛠️ Tech Stack & Architecture

### Backend Infrastructure
* **Language & Framework:** Python 3.10+, FastAPI, Uvicorn
* **Primary Database (Relational):** PostgreSQL (Users, Roles, Sites, Surveys)
* **Secondary Database (NoSQL):** MongoDB (Raw sensor payloads, camera trap metadata, audio logs)
* **Authentication:** JWT with Role-Based Access Control (RBAC) & Bcrypt password hashing
* **Containerization:** Docker, Docker Compose

### Machine Learning & Data Processing
* **Vision Models:** Ultralytics YOLOv8, PyTorch (ResNet50 / EfficientNetV2 with FP16 AMP training)
* **Audio Processing:** Librosa, Torchaudio, Mel-Spectrogram 2D CNNs
* **Spatial Analytics:** GeoPandas, XGBoost, Scikit-Learn

---

## 📊 Configured Datasets
1. **Camera Trap Imagery:** Snapshot Serengeti (`silviamatoke/serengeti-dataset`)
2. **Species Recognition:** iNaturalist 2021 Validation Dataset (`ml-inat-competition-datasets`)
3. **Bioacoustic Analysis:** BirdCLEF 2026 Dataset (`birdclef-2026`)
4. **Multi-Taxa Classification:** Animal Kingdom 90 (`sanadalali/animal-categories-90-masters-of-survival`)
5. **Spatial & Occurrence Records:** GBIF Species Occurrence Records (`anjalibarge2511/gbif-species-occurrence-records`)

---

## 📅 Development Roadmap & System Design

### 🔹 Day 1: System Blueprint & Requirements Analysis
* **SDLC Framework:** Agile / Scrum Framework (Iterative ML model training and backend integration)
* **Functional Requirements (FR):**
  * `FR-01`: JWT authentication and bcrypt password security.
  * `FR-02`: Role-Based Access Control (4 predefined roles).
  * `FR-03`: PostgreSQL CRUD operations for monitoring sites.
  * `FR-04`: MongoDB payload ingestion for unstructured sensor telemetry.
  * `FR-05`: Inference integration for vision and audio deep learning models.
* **Non-Functional Requirements (NFR):**
  * `NFR-01`: Sub-200ms database response latency; sub-2s AI batch inference latency.
  * `NFR-02`: Dual-DB horizontal scalability for millions of unstructured camera trap logs.
  * `NFR-03`: 60-minute JWT token expiration and CORS middleware protection.
  * `NFR-04`: Containerized service deployment ensuring high availability.

#### User Stories
* **Wildlife Researcher:** *"I want to upload image/audio batches to the AI engine so I can instantly classify species without manual sorting."*
* **Conservation Officer:** *"I want to view species population trends and maps to generate monthly conservation strategies."*
* **Forest Department Officer:** *"I want to register monitoring sites and camera trap locations linked to telemetry logs."*
* **Administrator:** *"I want to manage user permissions and monitor database health."*

#### System Workflow Analysis
```text
[ Field Sensors ] ─────────► (Camera Traps / Audio Recorders)
       │
       ▼
[ Ingestion Layer ] ───────► POST /api/v1/sensor/log ──► Store Raw Payload in MongoDB
       │
       ▼
[ AI Inference Engine ] ───► Vision (ResNet50/YOLOv8) + Audio (Mel-Spectrogram CNN)
       │
       ▼
[ Relational Storage ] ────► Link Predictions + GPS Coordinates ──► PostgreSQL Survey Record
       │
       ▼
[ Intelligence Dashboard ] ─► Interactive Heatmaps & Conservation Reports


