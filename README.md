# AI Agent Application

A modular, extensible AI Agent application built with Python, featuring an autonomous AI core, an API backend server, and an interactive frontend client UI.

---

## 📁 Project Structure

```text
.
├── .devcontainer/         # VS Code Remote Container configuration
│   └── devcontainer.json  # Dev container settings and extension definitions
├── .env                   # Local environment variables (DO NOT COMMIT)
├── .gitignore             # Standard git ignore list (includes .env, execution artifacts)
├── ai_agent.py            # Core AI logic, prompt engineering, and tool orchestration
├── backend.py             # API server application exposing service endpoints
├── frontend.py            # User interface application for client interactions
├── requirement.txt        # Python package dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Architecture Overview

The system follows a three-tier architecture separating interface, API orchestration, and AI reasoning logic:

- **`ai_agent.py`**: Houses the central autonomous agent logic, reasoning loops, memory state handling, and tool integrations (e.g., LLM prompts, function calling).
- **`backend.py`**: Acts as the API gateway and backend service provider, routing client requests to the AI agent and delivering responses back to the interface layer.
- **`frontend.py`**: Provides an intuitive web UI (e.g., Streamlit/Gradio/Web client) for users to send inputs, view real-time model outputs, and inspect conversation history.

---

## 💻 Prerequisites

Before setting up the project, ensure you have the following installed on your host machine:

- **Python**: Version `3.9` or higher
- **Git**: Latest release
- **Docker & VS Code** *(Optional)*: Required if you prefer running inside a VS Code Dev Container.

---

## 🚀 Setup & Installation

### Option 1: Local Setup (Recommended for standard Python workflows)

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

#### 2. Create and Activate a Virtual Environment
Using a virtual environment prevents global package pollution and guarantees reproducible dependency versions.

* **macOS / Linux:**
  ```bash
  python3 -m venv venv
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

#### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirement.txt
```

#### 4. Environment Configuration & Security Verification
Create a `.env` file in the project root directory by copying or creating a file based on template values below:

```env
# API Keys & Sensitive Secrets (DO NOT COMMIT TO GIT)
OPENAI_API_KEY=your_openai_api_key_here

# Application Service Configuration
PORT=8000
HOST=127.0.0.1
DEBUG=True
```

> **🔒 CRITICAL SECURITY CHECK:**  
> Verify that `.env` is listed in your `.gitignore` file before running any `git add` or `git commit` commands. Never hardcode API keys or commit secrets to public or private source control repositories.

---

### Option 2: Setup via VS Code Dev Container

If you prefer containerized development using Docker and VS Code:

1. Open **VS Code**.
2. Install the **Dev Containers** extension (`ms-vscode-remote.remote-containers`).
3. Open the project repository folder in VS Code.
4. When prompted in the lower-right corner, click **"Reopen in Container"** (or press `F1`, type `Dev Containers: Reopen in Container`, and press `Enter`).
5. VS Code will build the container image and install required packages automatically.
6. Create your local `.env` file in the root folder as described in step 4 above.

---

## 🚦 Running the Application

> **⚠️ Dependency Sequence Notice:**  
> The `frontend.py` interface communicates directly with the `backend.py` API server. **You must start the backend server first** before launching the frontend client.

### Step 1: Start the Backend Service
Open a terminal (with your virtual environment activated) and execute:

```bash
python backend.py
```

*Expected output:* The server will start and listen for requests on `http://127.0.0.1:8000` (or the `PORT` specified in your `.env` file).

### Step 2: Start the Frontend Interface
Open a **second terminal session**, activate your virtual environment, and execute:

```bash
python frontend.py
```

*Expected output:* The frontend user interface will initialize and connect to the running backend service. Access the interface via your browser at the local URL printed in the terminal (typically `http://localhost:8501` or `http://localhost:7860`).

---

## 🔍 Troubleshooting & Common Issues

### 1. Missing `.env` File or Key Error (`KeyError: 'OPENAI_API_KEY'`)
* **Symptom:** Application crashes at startup with an environment variable error or `KeyError`.
* **Resolution:** 
  1. Confirm that a file explicitly named `.env` exists in the project root folder.
  2. Verify that all required keys (e.g., `OPENAI_API_KEY=sk-...`) are defined without quotes or extra whitespace.
  3. Ensure that python packages like `python-dotenv` are loading variables correctly upon application startup.

### 2. Connection Refused / Frontend Cannot Reach Backend
* **Symptom:** Frontend displays connection timeout, network error, or `ConnectionRefusedError`.
* **Resolution:**
  1. Verify `backend.py` is currently running in an active terminal window.
  2. Check that `backend.py` and `frontend.py` are using matching port configurations (`HOST` and `PORT` settings in `.env`).
  3. Check local firewall settings if connecting across different containers or host interfaces.

### 3. Residual Execution Artifacts
* **Symptom:** Workspace clutter or unexpected behavior caused by temporary execution artifacts like `tempCodeRunnerFile.py` or `__pycache__/`.
* **Resolution:** Ensure standard ignore rules are included in `.gitignore`:
  ```text
  .env
  tempCodeRunnerFile.py
  __pycache__/
  *.pyc
  venv/
  .vscode/
  ```

---

## 🔒 Security Best Practices

1. **Development vs. Production:** Settings like `DEBUG=True` and permissive CORS origins are for local testing only. Ensure `DEBUG` is set to `False` in staging and production environments.
2. **Secret Management:** Do not output active API keys into console logs or user-facing error messages.
3. **No Privileged Execution:** Do not run startup commands or scripts using `sudo` or root privileges.