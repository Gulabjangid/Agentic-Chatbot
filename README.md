# Agentic Chatbot AI Application

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-ready-brightgreen.svg)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io/)

A modular, production-ready AI Agent application built with Python 3.11, featuring an autonomous reasoning agent engine, a high-performance FastAPI backend server, and an interactive Streamlit frontend web interface.

---

## 📁 Repository Overview

```text
.
├── .devcontainer/         # VS Code Remote Container configuration
│   └── devcontainer.json  # Dev container settings and extension definitions
├── .github/workflows/     # CI/CD pipeline definitions
│   └── ci.yml             # Continuous Integration workflow
├── .env                   # Local environment configuration file (ignored by Git)
├── Dockerfile             # Container image build instructions
├── docker-compose.yml     # Multi-container service orchestration
├── ai_agent.py            # AI Agent core reasoning, tool invocation, and state management
├── backend.py             # FastAPI REST service & API gateway exposing endpoints
├── frontend.py            # Interactive Streamlit client web user interface
├── requirement.txt        # Primary Python package dependencies
└── README.md              # Project documentation and operational guide
```

---

## 🛠️ System Architecture

The application is structured around a decoupled three-tier architecture:

1. **AI Agent Core (`ai_agent.py`)**: Houses autonomous decision-making loops, tool execution routines, prompt templates, and integrations with external LLM providers (e.g., OpenAI, Groq) and search services (e.g., Tavily).
2. **Backend API Gateway (`backend.py`)**: A FastAPI application running on Uvicorn (port `8000`) that processes client payloads, manages backend state, handles `/health` checks, and exposes interactive OpenAPI documentation.
3. **Frontend UI (`frontend.py`)**: A Streamlit web interface (port `8501`) providing chat interactions, session control, agent output formatting, and API status monitoring.

---

## 💻 Prerequisites

Ensure your development workstation meets the following minimum requirements:

- **Python**: Version `3.11` or higher installed locally.
- **Docker Engine & Docker Compose**: Docker Desktop (Windows/macOS) or Docker Engine v20.10+ with Compose V2 plugin (Linux).
- **Git**: Installed for version control.

---

## ⚙️ Environment Configuration

Before launching the services via Docker Compose or local execution, you **must create a `.env` configuration file** in the project root directory.

### Step 1: Create `.env` File

Copy or create a `.env` file in the root folder:

```bash
# Unix / macOS
touch .env

# Windows (PowerShell)
New-Item -ItemType File -Name .env -Force
```

### Step 2: Populate Environment Variables

Add your API keys and configuration parameters to `.env`:

```env
# AI Provider API Keys
OPENAI_API_KEY=sk-proj-your-openai-key-here
GROQ_API_KEY=gsk_your_groq_key_here
TAVILY_API_KEY=tvly-your-tavily-key-here

# Server & Host Settings
HOST=0.0.0.0
PORT=8000
DEBUG=True

# Backend Communication Endpoint (Used by Streamlit Frontend)
BACKEND_URL=http://127.0.0.1:8000
```

> ⚠️ **CRITICAL NOTE:**  
> Never commit your `.env` file or hardcode secret keys into source code. Verify `.env` is listed in `.gitignore`.

---

## 🚀 Execution Path 1: Docker Compose (Recommended)

Docker Compose orchestrates the containerized build and execution of all system services in an isolated environment.

### 1. Build and Start Services

Launch the application containers in detached mode:

```bash
docker compose up --build -d
```

### 2. Verify Running Containers

Check service status to verify the backend and frontend containers are active:

```bash
docker compose ps
```

### 3. Verify Container Health

Query the backend health check endpoint:

* **Unix / macOS / Linux:**
  ```bash
  curl -s http://localhost:8000/health
  ```

* **Windows PowerShell:**
  ```powershell
  Invoke-RestMethod -Uri http://localhost:8000/health
  ```

* **Expected Output:**
  ```json
  {"status": "ok"}
  ```

### 4. Stop and Clean Up Services

To gracefully stop and remove running containers, networks, and volumes:

```bash
docker compose down
```

---

## 🐍 Execution Path 2: Local Native Setup (Non-Docker)

For local development or direct Python debugging without Docker:

### 1. Create and Activate a Python 3.11 Virtual Environment

* **macOS / Linux:**
  ```bash
  python3.11 -m venv venv
  source venv/bin/activate
  ```

* **Windows (Command Prompt):**
  ```cmd
  python -m venv venv
  venv\Scripts\activate.bat
  ```

* **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

### 2. Install Project Dependencies

Upgrade package manager and install dependencies:

```bash
pip install --upgrade pip
pip install -r requirement.txt
```

> **Dependency Note:** If working with standalone backend submodules, always install dependencies from the root `requirement.txt` to maintain version parity across `ai_agent.py`, `backend.py`, and `frontend.py`.

### 3. Start the Backend API Service

Start the backend application with Uvicorn on port `8000`:

```bash
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
```

*Alternatively, execute directly using Python:*
```bash
python backend.py
```

### 4. Start the Frontend UI Service

In a **separate terminal window** (with virtual environment activated):

```bash
streamlit run frontend.py
```

---

## 📍 Service Access & Verification Points

Once the services are running (via Docker or native Python execution), access the applications at the following endpoints:

| Touchpoint / Interface | Access URL | Description |
| :--- | :--- | :--- |
| **Backend Health Check** | [http://localhost:8000/health](http://localhost:8000/health) | REST verification route returning service status. |
| **Interactive API Docs** | [http://localhost:8000/docs](http://localhost:8000/docs) | OpenAPI (Swagger) browser interface for testing routes. |
| **Frontend Application UI** | [http://localhost:8501](http://localhost:8501) | Streamlit web client interface for interacting with the AI Agent. |

---

## 🔍 Troubleshooting & Frequently Asked Questions

### 1. Missing `.env` File Error
* **Symptom:** Application fails on startup with `KeyError: 'OPENAI_API_KEY'` or warnings regarding missing environment secrets.
* **Solution:** Create `.env` in the root folder as shown in [Environment Configuration](#%EF%B8%8F-environment-configuration). When using Docker Compose, verify that `.env` resides in the same directory as `docker-compose.yml`.

### 2. Port `8000` or Port `8501` Conflicts
* **Symptom:** Error stating `[Errno 98] Address already in use` or `Bind for 0.0.0.0:8000 failed: port is already allocated`.
* **Solution:** Identify and stop the process currently occupying the port:
  * **macOS / Linux:**
    ```bash
    lsof -i :8000
    kill -9 <PID>
    ```
  * **Windows PowerShell:**
    ```powershell
    Get-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess | Stop-Process -Force
    ```
  * Alternatively, override default ports in your `.env` or adjust host port mapping in `docker-compose.yml`.

### 3. Docker Daemon Execution Failures
* **Symptom:** Command outputs `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`
* **Solution:** Ensure Docker Desktop is active and running in your system tray. On Linux environments, ensure the service is running via `sudo systemctl start docker` and your user belongs to the `docker` group (`sudo usermod -aG docker $USER`).

### 4. Dependency Mismatches or Imports Error
* **Symptom:** `ModuleNotFoundError` when executing standalone modules locally.
* **Solution:** Confirm your Python virtual environment is active (`(venv)` shown in prompt) and re-run `pip install -r requirement.txt`.

---

## 🔒 Security Best Practices

1. **Keep Secrets Safe:** Do not check credentials into version control. Ensure `.env` is listed in `.gitignore`.
2. **Production Mode:** Set `DEBUG=False` in staging or production deployments.
3. **Privilege Isolation:** Avoid running backend or frontend commands with `sudo` or administrator root privileges.